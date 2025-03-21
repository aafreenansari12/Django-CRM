import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'ansariaafreen98.'
)

# prepare a curson object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE aafreen")

print("All done!")