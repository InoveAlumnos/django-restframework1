from os import name
import requests
import json
import hashlib

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
url_base = 'http://gateway.marvel.com/v1/public/'
endpoint = 'comics'
print(hash.hexdigest())


# Realizamos un request, preparamos los parámetros de la petición:
params = dict(ts=ts, apikey=public_key, hash=hash.hexdigest())
url = url_base+endpoint
res = requests.get(url, params=params)
with open(f'{json_examples_dir}example.json', 'w') as file:
            json.dump(json.loads(res.text), file, indent=4)



def get_data(url, aditional_params={}, namefile='file', save=True):
    '''
    Return JSON object, and save a namefile.JSON in the disc
    '''
    params = dict(ts=ts, apikey=public_key, hash=hash.hexdigest())
    params.update(aditional_params)
    print('params', params)
    res = requests.get(url, params=params)
    if save:
        with open(f'{json_examples_dir}{namefile}.json', 'w') as file:
            json.dump(json.loads(res.text), file, indent=4)
    return json.loads(res.text)


# Ahora un ejemplo con limit y offset:

aditional_params = {'limit': 5, 'offset': 0}
params.update(aditional_params)
res = requests.get(url, params=params)
with open(f'{json_examples_dir}example_2.json', 'w') as file:
            json.dump(json.loads(res.text), file, indent=4)




# offset = 20
# limit = 10
# per_page = 5
# id = []
# description = []
# prices = []
# thumbnail = []
# last_id = 0

# while len(id) < per_page:
#     aditional_params = {'limit': limit, 'offset': offset}
#     comics = get_data(url=url_base+"comics",
#                   aditional_params=aditional_params, save=False)
#     comics_list = comics.get('data').get('results')

#     for comic in comics_list:
#         if comic.get('description') != None and comic.get('prices')[0].get('price') != 0.00:
#             last_id = comic.get('id')
#             id.append(last_id)
#             description.append(comic.get('description'))
#             prices.append(comic.get('prices')[0].get('price'))
#             thumbnail.append(
#                 f"{comic.get('thumbnail').get('path')}/standard_xlarge.jpg")
#     if len(id) < per_page:
#         id.clear()
#         description.clear()
#         prices.clear()
#         thumbnail.clear()
#         limit += 5

# tabla = '<div style="height:90%; width:90%; overflow:auto;"><table class="default">'

# for i in range(len(id)):
#     tabla += f'''
#     <tr>
#     <td><img src="{thumbnail[i]}"></td>
#     <td>{description[i]}</td>
#     <td>{prices[i]}</td>
#     <td>FAV</td>
#     <td>carrito</td>
#     </tr>
#     '''
# tabla += '</table></div>'

# print(tabla)

