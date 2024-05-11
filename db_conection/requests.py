# Параметри для підключення до бази даних MySQL
from db_conection.db_handler import MySQLDatabase
import json

# Відкриття файлу JSON
with open('db_const.json') as json_file:
    config_data = json.load(json_file)

# Отримання даних з файлу JSON
host = config_data['host']
username = config_data['username']
password = config_data['password']
database = config_data['database']


db = MySQLDatabase(host, username, password, database)
db.connect()


query = "SELECT * FROM Requests WHERE status = 'requested'"
data = db.fetch_data(query)
print("Data from MySQL database:")
for record in data:
    print(record)


db.disconnect()