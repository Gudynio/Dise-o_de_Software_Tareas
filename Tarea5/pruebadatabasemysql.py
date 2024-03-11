import mysql.connector
from database import *

#Clase de MySQL  
class MySQL(DataBase):
    _conexion = ""
    def __init__(self, servidor, usuario, contrasena ,basedatos):
        self.servidor = servidor
        self.usuario = usuario
        self.contrasena = contrasena
        self.basedatos = basedatos        
        
    def conectar(self):
        host = self.servidor
        user = self.usuario
        password = self.contrasena
        database = self.basedatos

        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            return connection

        except mysql.connector.Error as err:
            return(f"Error: {err}")

    def Crear_tabla(self, nombre):
        connection = self.conectar()

        if connection:
            try:
                # Crear un objeto cursor para ejecutar consultas SQL
                cursor = connection.cursor()

                insert_query = f"""CREATE TABLE {nombre} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255),
                fecha DATE
                )"""
                
                cursor.execute(insert_query)

                # Commit para aplicar los cambios
                connection.commit()
                return(f"New table '{nombre}' inserted successfully")
                
            except mysql.connector.Error as err:
                return(f"Error: {err}")

            finally:
                # Cerrar el cursor y la conexión en el bloque 'finally' para asegurar una limpieza adecuada
                if 'cursor' in locals() and cursor is not None:
                    cursor.close()

                if 'connection' in locals() and connection.is_connected():
                    connection.close()
        else:
            return("Error connecting to the database.")

    def abrir(self, fecha):
        connection = self.conectar()

        if connection:
            try:
                # Crear un objeto cursor para ejecutar consultas SQL
                cursor = connection.cursor()

                # Ejemplo: Realizar una consulta SELECT
                select_query = f"SELECT * FROM Reporte where  fecha=DATE('{fecha}')"
                cursor.execute(select_query)

                # Obtener todos los resultados de la consulta
                rows = cursor.fetchall()

                # Mostrar los resultados
                for row in rows:
                    print(row)

            except mysql.connector.Error as err:
                return(f"Error: {err}")

            finally:
                # Cerrar el cursor y la conexión en el bloque 'finally' para asegurar una limpieza adecuada
                if 'cursor' in locals() and cursor is not None:
                    cursor.close()

                if 'connection' in locals() and connection.is_connected():
                    connection.close()
        else:
            return("Error connecting to the database.")

    def insertar(self, tabla,nombre,fecha):
        connection = self.conectar()

        if connection:
            try:
                # Crear un objeto cursor para ejecutar consultas SQL
                cursor = connection.cursor()

                # Ejemplo: Insertar un nuevo registro en la tabla 'ejemplo'
                insert_query = f"INSERT INTO {tabla} (nombre, fecha) VALUES ('{nombre}','{fecha}')"
                cursor.execute(insert_query)

                # Commit para aplicar los cambios
                connection.commit()
                return(f"New record with nombre '{nombre}' and date {fecha} inserted successfully")

            except mysql.connector.Error as err:
                return(f"Error: {err}")

            finally:
                # Cerrar el cursor y la conexión en el bloque 'finally' para asegurar una limpieza adecuada
                if 'cursor' in locals() and cursor is not None:
                    cursor.close()

                if 'connection' in locals() and connection.is_connected():
                    connection.close()
        else:
            return("Error connecting to the database.")

    def eliminar(self,table, date):
        connection = self.conectar()

        if connection:
            try:
                # Crear un objeto cursor para ejecutar consultas SQL
                cursor = connection.cursor()

                # Ejemplo: Eliminar un registro de la tabla 'ejemplo'
                delete_query = f"DELETE FROM {table} WHERE fecha = DATE('{date}')"
                cursor.execute(delete_query)

                # Commit para aplicar los cambios
                connection.commit()
                return(f"Record with date {date} deleted successfully")

            except mysql.connector.Error as err:
                return(f"Error: {err}")

            finally:
                # Cerrar el cursor y la conexión en el bloque 'finally' para asegurar una limpieza adecuada
                if 'cursor' in locals() and cursor is not None:
                    cursor.close()

                if 'connection' in locals() and connection.is_connected():
                    connection.close()
        else:
            return("Error connecting to the database.")

    def actualizar(self, tabla,nombre,date):
        connection = self.conectar()

        if connection:
            try:
                # Crear un objeto cursor para ejecutar consultas SQL
                cursor = connection.cursor()

                # Ejemplo: Insertar un nuevo registro en la tabla 'ejemplo'
                insert_query = f"UPDATE {tabla} SET nombre = '{nombre}'  WHERE fecha = DATE('{date}')"
                cursor.execute(insert_query)

                # Commit para aplicar los cambios
                connection.commit()
                return(f"Record with nombre '{nombre}' and date {date} update successfully")

            except mysql.connector.Error as err:
                return(f"Error: {err}")

            finally:
                # Cerrar el cursor y la conexión en el bloque 'finally' para asegurar una limpieza adecuada
                if 'cursor' in locals() and cursor is not None:
                    cursor.close()

                if 'connection' in locals() and connection.is_connected():
                    connection.close()
        else:
            return("Error connecting to the database.")
        




# Uso de las funciones con los nuevos valores
#insertar_registro("Reporte","test3","2024-03-10")
