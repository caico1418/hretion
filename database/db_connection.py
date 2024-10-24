import mysql.connector

class DatabaseConnection:
    def __init__(self, host, username, password, database):
        # define values of database
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()  # Corrección aquí
            print("Conexión correcta")
        except mysql.connector.Error as err:
            print(f'Error al conectarse a la base de datos {err}')
            self.connection = None

    # Check Data
    def selectData(self):  # Corrección del nombre
        if self.connection and self.cursor:
            try:
                self.cursor.execute("SELECT * FROM USERS")
                result = self.cursor.fetchall()  # Recoger los resultados
                return result
            except mysql.connector.Error as err:
                print(f'Error al ejecutar la consulta {err}')

    def selectDataName(self, name):
        if self.connection and self.cursor:
            try:
                # Consultar los nombres existentes en la tabla 'users'
                self.cursor.execute("SELECT FIRST_NAME FROM users")
                result = self.cursor.fetchall()

                # Crear una lista de nombres
                user_names = [row[0] for row in result]

                # Devolver True si el nombre ya existe
                return name in user_names

            except Exception as e:
                print(f"Error en la consulta de usuario: {e}")
                return False

     # validar haya un registro duplicado en la base de datos
    def duplicated(self, fullName, hotelName, phoneNumber, mail):
        if self.connection and self.cursor:
            try:
                # Consulta para verificar duplicados en cualquiera de los campos
                query = """
                    SELECT FULL_NAME, NAME_HOTEL, PHONE_NUMBER, MAIL 
                    FROM registerMainUser 
                    WHERE FULL_NAME = %s OR NAME_HOTEL = %s OR PHONE_NUMBER = %s OR MAIL = %s
                """
                params = (fullName, hotelName, phoneNumber, mail)
                self.cursor.execute(query, params)
                result = self.cursor.fetchall()

                # Si encuentra algún registro, significa que hay duplicados
                if result:
                    return True  # Hay duplicados
                else:
                    return False  # No hay duplicados

            except Exception as e:
                print(f"Error al realizar la acción de validar duplicado: {e}")
                return False

    # Insert data
    def insertData(self, query, params=None):
        if self.connection and self.cursor:
            try:
                if params is None:
                    params = ()
                self.cursor.execute(query, params)
                self.connection.commit()
            except mysql.connector.Error as err:
                print(f'Error al ejecutar la query {err}')



    # Cerrar la conexión
    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
            print("Conexión cerrada correctamente")
        except mysql.connector.Error as err:
            print(f'Error al cerrar la conexión {err}')


