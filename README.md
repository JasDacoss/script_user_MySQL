
<h1 align="center"> Creación de Usuarios en MySQL con Python y SQL </h1>

En un script de MySQL me he embarcado,
creando usuarios con datos solicitados.
Por pantalla se pide lo necesario con cuidado,
en la base de datos, nuevos usuarios han llegado.

## `1.` INTRODUCCIÓN
El siguiente proyecto se enfoca en la automatización de tareas utilizando Python y SQL, específicamente en un script que interactúa con una base de datos MySQL. En este proyecto, se ha desarrollado un sistema que permite la creación y eliminación automatizada de usuarios en la base de datos MySQL a través de un script escrito en Python. Esta automatización en SQL mediante Python agiliza y simplifica el proceso de administración de usuarios, reduciendo posibles errores manuales y garantizando la integridad de los datos en la base de datos. Al utilizar Python para interactuar con SQL, se aprovechan las capacidades de ambos lenguajes para mejorar la eficiencia y productividad del sistema informático.

## `2.` DESARROLLO
Lo primero fue buscar una librería en Python que permitiera la conexión y manipulación de bases de datos desde Python. La elegida fue PyMySQL porque decidí trabajar con el gestor MySQL y  es un paquete de Python que permite interactuar con bases de datos MySQL. 

    import pymysql

El proceso comenzó con la conexión a la base de datos especificando el host, usuario, contraseña y base de datos a utilizar.

    conn = pymysql.connect(host='localhost', user='tu_usuario', password='tu_contraseña', database='mysql')
    cursor = conn.cursor()

Definí 3 funciones diferentes para interactuar con la base de datos: 

1. `crear_usuario():` Solicitar al usuario el nombre y la contraseña del nuevo usuario a crear. Estos datos se utilizan para construir una consulta SQL que crea un nuevo usuario en la base de datos con los parámetros proporcionados. Una vez generada la consulta, se ejecuta utilizando el cursor y se confirman los cambios en la base de datos mediante conn.commit(). Durante la ejecución del script, se muestra un mensaje indicando el nombre del usuario recién creado.
2. `eliminar_usuario():` Solicita al usuario el nombre del usuario a eliminar, luego ejecuta una consulta SQL como la función anterior para eliminar dicho usuario. Una vez generada la consulta, se ejecuta utilizando el cursor y se confirman los cambios en la base de datos mediante conn.commit(). Durante la ejecución del script, se muestra un mensaje indicando el nombre del usuario recién eliminado.
3. `mostrar_usuarios():` Ejecuta una consulta SQL para mostrar todos los usuarios existentes en la base de datos. Una vez generada la consulta, se ejecuta utilizando el cursor. Se recuperan los resultados de la consulta con cursor.fetchall() y se muestran los nombres de usuario existentes en la base de datos.

Se implementó un bucle que muestra un menú con opciones para crear un usuario, eliminar un usuario, mostrar usuarios o salir del programa. Dependiendo de la opción seleccionada por el usuario, se llama a la función correspondiente.

Finalmente, al completar el proceso de creación de usuarios, se cierra la conexión a la base de datos para mantener una gestión adecuada de los recursos.

## `2.` ERRORES DURANTE EL PROYECTO
Al empezar este proyecto y por consiguiente el script se tomó la decisión de trabajar con PostgreSQL. Pero intentando ejecutar el script me daba muchos errores de la conexión a la base de datos. Al tomar la decisión de cambiar al gestor MySQL ya no apareció ningún error. Aún no se sabe si es porque la librería relacionada con PostgreSQL estaba mal utilizada o es más complicado conectar Python con este gestor. 
