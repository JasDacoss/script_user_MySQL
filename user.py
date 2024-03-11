import pymysql

# Conectar a la base de datos
conn = pymysql.connect(host='localhost', user='tu_usuario', password='tu_contraseña', database='mysql')
cursor = conn.cursor()


def crear_usuario():
    # Solicitar nombre del usuario
    nombre = input("Nombre del usuario: ")

    # Solicitar contraseña del usuario
    contrasena = input("Contraseña del usuario: ")

    # Consulta SQL para crear un nuevo usuario con contraseña
    sql = f"CREATE USER '{nombre}'@'localhost' IDENTIFIED BY '{contrasena}';"

    # Ejecutar la consulta SQL
    cursor.execute(sql)

    # Confirmar los cambios en la base de datos
    conn.commit()

    # Mostrar el nombre ingresado
    print(f"Usuario creado: {nombre}")


def eliminar_usuario():
    # Solicitar nombre del usuario a eliminar
    nombre = input("Nombre del usuario a eliminar: ")

    # Consulta SQL para eliminar un usuario
    sql = f"DROP USER '{nombre}'@'localhost';"

    # Ejecutar la consulta SQL
    cursor.execute(sql)

    # Confirmar los cambios en la base de datos
    conn.commit()

    print(f"Usuario eliminado: {nombre}")


def mostrar_usuarios():
    # Consulta SQL para mostrar todos los usuarios
    sql = "SELECT User FROM mysql.user WHERE Host='localhost';"

    # Ejecutar la consulta SQL
    cursor.execute(sql)

    # Obtener y mostrar los resultados
    usuarios = cursor.fetchall()

    print("Usuarios existentes:")
    for usuario in usuarios:
        print(usuario[0])


# Menú principal en bucle
while True:
    print("\n--- Menú ---")
    print("1. Crear un usuario")
    print("2. Eliminar un usuario")
    print("3. Mostrar usuarios")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        crear_usuario()

    elif opcion == '2':
        eliminar_usuario()

    elif opcion == '3':
        mostrar_usuarios()

    elif opcion == '4':
        break

# Cerrar la conexión
conn.close()
