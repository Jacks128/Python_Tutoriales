#pip install mysql-connector-python
#ejecutar comando de arriba para llamar ala libreria para poder ejecutar la conexion
import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='Inge1718',
        db='gamesdb'
    )
    if conexion.is_connected():
        print("Conexion Exitosa")
        infoServer = conexion.get_server_info()
        print("Informacion del servidor: ", infoServer)
except Error as ex:
    print("Error de conexion", ex)
finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexion ha finalisado")
#Esta es la estrucutra básica para hacer la conexion a una base de datos en mysql desde python