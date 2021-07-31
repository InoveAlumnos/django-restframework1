from os import name
import requests
import json
import hashlib

# NOTE:
# Archivo de muestra de algoritmo para vista personalizada de API para comprar comics, 
# primero consultamos los comics disponibles en la página de Marvel, 
# luego generamos una lista de los que tienen precio y descripción, 
# porque varios vienen `null`.

# NOTE: información sobre tablas HTML: https://www.w3schools.com/html/html_tables.asp 

# Directorio para guardar los ejemplos:
json_examples_dir = 'tools/api_json_examples/'


# Obtenemos los datos de la pagina de apis de marvel: https://developer.marvel.com/ 
public_key = '58ee40376f7c10e99f440f5e3abd2caa'
private_key = '2c0373e00d85edb4560f68ddc2094014e8694f90'
ts = 1
# Obtenemos el "hash":
to_hash = str(ts)+private_key+public_key
hash = hashlib.md5(to_hash.encode())

# Establecemos la url_base y el endpoint:
URL_BASE = 'http://gateway.marvel.com/v1/public/'
ENDPOINT = 'comics'
print(hash.hexdigest())


# Realizamos un request, preparamos los parámetros de la petición:
PARAMS = dict(ts=ts, apikey=public_key, hash=hash.hexdigest())
# Declaramos nuestras variables:
id = []
title = []
description = []
prices = []
thumbnail = []
limit = 1
offset = 0

# Realizamos el request:
aditional_params = {'limit': limit, 'offset': offset}
params = PARAMS
params.update(aditional_params)
# NOTE: A los parametros de hash, api key y demás, sumamos limit y offset para paginación.
res = requests.get(URL_BASE+ENDPOINT, params=params)
comics = json.loads(res.text)

# Obtenemos la lista de comics:
comics_list = comics.get('data').get('results')

# Filtramos la lista de comics y nos quedamos con lo que nos interesa:
for comic in comics_list:
    id.append(comic.get('id'))
    description.append(comic.get('description'))
    title.append(comic.get('title'))
    prices.append(comic.get('prices')[0].get('price'))
    thumbnail.append(
        f"{comic.get('thumbnail').get('path')}/standard_xlarge.jpg")

# NOTE: Construimos la tabla, concatenando en un string el código HTML:

# Abrimos el template:
template = '''<div>
<div style="height:90%; width:90%; overflow:auto;background:gray;">
    <table>'''

# Generamos el for para construir las tablas en html:
for i in range(len(id)):
    
    # Primero validamos los datos de descripción y precio, si no están, ponemos un mensaje por defecto:
    if description[i] == None:
        desc = "<h3>Description Not Available<h3>"
    else:
        desc = description[i]

    if prices[i] == 0.00:
        # Con este condicional inhabilitamos la compra de los comics sin precio.
        price = "<h3>N/A<h3>"
        visibility = "hidden"
    else:
        price = prices[i]
        visibility = "visible"

    # Una vez validados los datos en las variables, vamos completando el template con las variables:
    # <tr> </tr> --> "table row" contiene la FILA de la tabla
    # <td> </td> --> "table data" contiene el DATO de la celda
    # Se agrupan:
    # <tr> <td> el dato acá </td> </tr>

    # La estructura de la tabla es:
    # <tr>
    #     <td> imagen </td>
    #     <td> titulo </td>
    #     <td> precio </td>
    #     <td> formulario de compra </td>
    # </tr>

    
    template += f'''
    <tr>
    <td>
        <img src="{thumbnail[i]}">
    </td>
    <td>    
        <h2>{title[i]}</h2><br><br>
        {desc}
    </td>
    <td><h2>U$S{price}</h2></td>
    <td>
        <form action="http://localhost:8000/e-commerce/purchased_item/" method="post" , style ="visibility: {visibility};">
            <label for="qty"><h3>Enter Quantity:</h3></label>
            <input type="number" id="qty" name="qty" min="0" max="15">
            <input type="submit" value="Buy" >
            <input type="text" name="id" value="{id[i]}" style="visibility: hidden">
            <input type="text" name="title" value="{title[i]}" style="visibility: hidden">
            <input type="text" name="thumbnail" value="{thumbnail[i]}" style="visibility: hidden">
            <input type="text" name="description" value="{description[i]}" style="visibility: hidden">
            <input type="text" name="prices" value="{prices[i]}" style="visibility: hidden">
        </form>
    </td>
    </tr>
    '''
# NOTE: sobre formularios HTML: https://www.w3schools.com/html/html_forms.asp

# Cierro el template:
template += f'</table></div></div>'

# Imprimimos por consola el HTML construido (se puede probar en https://codepen.io/):
print(template)
# O lo podemos guardar en un HTML, como el nombre no cambia, el archivo se pisa en cada petición:
f = open('tools/html_rendered/get_comics.html','w')
f.write(template)
f.close