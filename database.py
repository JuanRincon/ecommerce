"""
import mysql.connector

database = mysql.connector.connect(
        host='127.0.0.1',
		port='33061',
        user='root',
        password='Socrates123*',
        database='ecommerce'
)



import mysql.connector

database = mysql.connector.connect(
		host="localhost",
		port="33061",
        user="root",
        password="Socrates123*", 
		database="mysql"

)

database.close()

from mysql.connector import pooling

dbconfig = {
    "host": "localhost",
	"port": "33061",
    "user": "root",
    "password": "Socrates123*",
    "database": "prueba"
}

pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=10, **dbconfig)

connection = pool.get_connection()

"""

import mysql.connector
from mysql.connector import errors

def connect_to_db():
    try:
        return mysql.connector.connect(
            host="localhost",
			port="33061",
            user="root",
            password="Socrates123*", 
			database="ecommerce"
        )
    except errors.OperationalError as e:
        print("Connection error:", e)
        return None

connection = connect_to_db()

from mysql.connector import errors

# If connection fails, you can try reconnecting in a loop or handle accordingly
if connection is None:
    print("Reconnection failed.")
else:
    print("Connection successful.")

def from_db():
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM productos")
	myresult = cursor.fetchall()
	#Convertir los datos a diccionario
	insertObject = []
	columnNames = [column[0] for column in cursor.description]
	for record in myresult:
		insertObject.append(dict(zip(columnNames, record)))
	cursor.close()
	return insertObject

def for_catalog():
	iden = open("./static/dbase.js", "w")
	iden.write(f"export const dbase = {from_db()}")
	iden.close()
