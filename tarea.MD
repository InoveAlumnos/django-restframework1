![Inove banner](/inove.jpg)
Inove Escuela de Código\
info@inove.com.ar\
Web: [Inove](http://inove.com.ar)

---
# Tarea: Django - Django REST FRAMEWORK 1

Al realizar esta tarea pondremos en práctica los conocimientos adquiridos en clase.
Una vez finalizada, el alumno debe subir el enlace a su repositorio "forkeado" el foro de tarea correspondiente -NO SE ADMITE LA DEVOLUCIÓN POR OTRO CANAL SALVO SE ESPECIFIQUE LO CONTRARIO- 

Recuerde que no debe subir la base de datos al sistema, para ello se encuentra el archivo .gitignore que especifica los archivos y directorios omitidos.

---

### 1. Utilizar el proyecto de "Marvel" visto en clase.
Inicializar el contenedor de docker, compilar la imagen del repositorio con:
**$** `docker-compose up`


### 2. Realizar las migraciones del sistema.
Recuerde que para poder comenzar a utilizar el Django Admin, es necesario que el sistema se encuentre alineado con la base de datos. Para ello debemos realizar las migraciones de la aplicación y crear un nuevo superusuario.
Los comandos necesarios se encuentran detallados en el archivo README.md

### 3. Familiarícese con el proyecto "marvel".
Recorra los directorios, incluso el directorio "tools" que sirve como muestra del proceso de consumo de datos en el servicio de Marvel. Recuerde que el objetivo de consumir estos datos es para llenar la base de datos y llenar nuestro stock de comics.
También vea cómo se realizaron las APIs de la aplicación e_commerce, los archivos relacionados, librerías y urls. 

### 4. Instale Django REST Framework (DRF) en "ejercicios_practica".
En ejercicios_practica se encuentra el proyecto avanzado hasta la clase 3, debe incluir los cambios necesarios para incluir DRF en el proyecto (declararlos en settings.py etc;) puede guiarse por el ejemplo de clase para ello.

### 5. Agregue la carpeta "api" a su aplicación e_commerce.
Agregue la carpeta "api" a su aplicación e_commerce al igual que en el ejemplo de clase, y desarrolle al menos 3 vistas de API con decoradores. Las vistas deben ser de tipo GET y POST. Luego debe asignarles las URLs para darles acceso. Proponga una lógica de negocio para cada una de ellas (basta con un print de algún parámetro pasado por request)

### 6. Copie el archivo "marvel_api_views.py" a su carpeta de api.
Copie el archivo "marvel_api_views.py" a su carpeta de api, trate de entender la lógica de negocio de ambas vistas (get_comics, y purchased_item) y haga que funcione en el proyecto de práctica.

### 7. Incorpore el paginado en la vista "get_comics".
Incorpore el paginado en la vista "get_comics", de manera que por medio de una petición de tipo GET se envíen los parámetros "limit" y "offset" (es posible obviar el parámetro "limit"). 
Recomendamos utilizar un formulario con dos botones de submit que envíen estos parámetros al final de la página.

---

## ¿Dudas?
Ante cualquier inquietud, debe referirse a los canales especificados para su trato en Inove.