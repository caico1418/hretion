from database.db_connection import DatabaseConnection
from tkinter import messagebox

data = DatabaseConnection('127.0.0.1', 'root', '', 'hretion')


def registerUser(fullName, hotelName, phoneNumber, mail, password):
    try:
        # Conectar a la base de datos
        data.connect()
        if data.connection:
            result = data.duplicated(fullName, hotelName, phoneNumber, mail)
            if result:
                messagebox.showinfo('info', 'Registro existente')
            else:
                # Registrar el usuario en la tabla registerMainUser
                query = """
                    INSERT INTO registerMainUser (FULL_NAME, NAME_HOTEL, PHONE_NUMBER, MAIL) 
                    VALUES (%s, %s, %s, %s)
                """

                # Validar que no haya un registro duplicado en la bd

                params = (fullName, hotelName, phoneNumber, mail)
                data.insertData(query, params)
                print(f"Registro de {fullName} exitoso en registerMainUser.")

                # Usar el primer nombre para crear el usuario en la tabla de MySQL
                name = fullName.split()[0]  # Tomar el primer nombre
                createUser(name, password)  # Crear el usuario

    except Exception as e:
        print(f"Error al registrar el usuario {fullName}: {e}")
        messagebox.showerror('Error', f'No se pudo registrar el usuario: {e}')

    finally:
        # Asegurarse de cerrar la conexión
        if data.connection:
            data.close()


def createUser(name, password):
    try:
        # Asegurarse de que la conexión esté abierta
        data.connect()
        if data.connection:
            # Verificar si el nombre de usuario ya existe
            if data.selectDataName(name):
                messagebox.showerror('Error', 'Usuario ya existente. No se intentará crear de nuevo.')
                return  # Salir de la función si el usuario ya existe

            # Crear el usuario en la base de datos MySQL
            query = f"CREATE USER '{name}'@'localhost' IDENTIFIED BY '{password}';"
            data.cursor.execute(query)

            # Asignar todos los privilegios al usuario
            grant_privileges_query = f"GRANT ALL PRIVILEGES ON hretion.* TO '{name}'@'localhost';"
            data.cursor.execute(grant_privileges_query)

            # Aplicar los cambios de permisos
            data.cursor.execute("FLUSH PRIVILEGES;")

            # Registrar el nuevo usuario en la tabla 'users'
            query = "INSERT INTO users (FIRST_NAME, `PASSWORD`) VALUES (%s, %s)"
            params = (name, password)
            data.insertData(query, params)

            messagebox.showinfo('Success', f"Tu Usuario creado con éxito es -> [ '{name}' ]")


    except Exception as e:
        print(f"Error al crear el usuario '{name}': {e}")
        messagebox.showerror('Error', f'No se pudo crear el usuario: {e}')

    finally:
        if data.connection:
            data.close()





