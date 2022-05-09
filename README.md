# [Proyecto Finanzas Personales - Sergio Gomez - 27620]


<br />

> Caracteristicas

- Diseño basado en Bootstrap
- Dashboard con graficos e info destacada (en proceso)
- Formularios de carga
- Formulario de busqueda


<br />


## ✨ Instrucciones



# Instalar requerimientos - SQLite 
pip3 install -r requirements.txt

# Crear tablas y migrar
python manage.py makemigrations
python manage.py migrate

# iniciar el servidor en modo debug
python manage.py runserver # default port 8000

# acceder al servidor : http://127.0.0.1:8000/
 
 Una vez que el servidor de Django esta corriendo hay que crear primero la/s cuenta/s y luego las categorias de gastos.# En la barra lateral de navegación hay un link "configuracion" para cargar las cuentas y las categorias
 una vez cargada las cuentas y categorias ya podemos empezar a cargar los gastos e ingresos

```





