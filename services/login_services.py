from tkinter import messagebox
from database.db_connection import DatabaseConnection


data = DatabaseConnection('127.0.0.1', 'root', '', 'hretion')


def validated_login(user, password):
    try:
        data.connect()
        if data.connection:
            # ver los valores del campo usuario
            query = "SELECT FIRST_NAME, `PASSWORD` FROM USERS WHERE FIRST_NAME = %s"
            data.cursor.execute(query, (user,))
            result = data.cursor.fetchone()

            if result:
                resultUser, resultPassword = result

                # validar usuario y contraseña
                if resultUser == user and resultPassword == password:
                    messagebox.showinfo('Success', 'Iniciando Sesion')

                else:
                    messagebox.showerror('Failed', 'Usuario o contraseña, No son correctos')
            else:
                messagebox.showerror('Failed', 'Usuario no encontrado')

    except Exception as e:
        print(f'Error en la conexion {e}')