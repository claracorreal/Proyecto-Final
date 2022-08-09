# Proyecto Final del curso de Python - Coderhouse


[Carpeta Test/Video](https://drive.google.com/drive/folders/1eltTw5lLZWq-fCU1LgbZesDS-CX8GHEU?usp=sharing)
[Documentación Django](https://docs.djangoproject.com/)

Este proyecto tiene como objetivo crear un sistema para la administración de Bebidas, Entradas, Platos y Postres. Al loguearte como empleados podrás:

- Crear, leer y actualizar Usuarios.
- Crear, leer, actualizar y eliminar artículos.
- Añadir una imagen para cada artículo.






# Instalación


Para poder instalar esta aplicación en tu computadora necesitas lo siguiente:



Comprobar versión de **Python**

>Este proyecto ha sido creado con Python 3.9.12, por lo que para su correcto funcionamiento recomendamos igual versión o superior para no tener problemas en las compatibilidades

>Verficar la versión en su ordenador ( Windows 10/11):

```
Python --version
Python 3.9.12
```

En ventanas:

```
c:\> py --version
c:\> Python 3.9.12
```




# Instalar dependencias

>Para instalar las dependencias, debe ejecutar **pip install**, asegúrese de estar en la carpeta del proyecto y pueda ver el **requirements.txt** archivo cuando haga **ls** o **dir**:

```
pip install -r requirements.txt
```

*Luego de correr este bloque de código, comenzará una instalación que durará un breve tiempo*

Configuración de la aplicación Django

>Una vez que termine la instalación de las dependencias, debe ejecutar algunos comandos Django:





# Migraciones

```
python mananage.py migrate
```

En ventanas:

```
c:\> py mananage.py migrate
```

# Proceso de Carga de las catergorias del menú

Para poder cargar de manera manual en el */Admin* deberá seguir el siguiente orden de referencia:

>1= **Entrada** 
>2= **Plato**
>3= **Postre**
>4= **Bebida**

# Ejecutar el servidor


```
python mananage.py runserver
```

En ventanas:

```
c:\> py mananage.py runserver
```

En la terminal de bash, si todo esta bien instalado, le dara la posibilidad de abrir el LocalHost, deberia verse de esta forma:


```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Luego de estos comandos, y una vez posicionado en la web, deberia poder correr el proyecto sin ningun problema.
