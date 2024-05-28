# Параметри для підключення до бази даних MySQL
import os

from dotenv import load_dotenv

from logic.db_conection.db_handler import MySQLDatabase
'''import json
json_file_path = os.path.join(os.path.dirname(__file__), 'db_const.json')
# Відкриття файлу JSON
with open(json_file_path) as json_file:
    config_data = json.load(json_file)


# Отримання даних з файлу JSON
host = config_data['host']
username = config_data['username']
password = config_data['password']
database = config_data['database']'''


load_dotenv()
host = os.getenv('DB_HOST')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_DATABASE')
db = MySQLDatabase(host, username, password, database)


def get_urls_emails():
    db.connect()
    query = "SELECT url,email,id FROM Requests WHERE status = 'requested'"
    data = db.fetch_data(query)
    db.disconnect()
    return data

def set_status_result(url, email, status, result):
    db.connect()
    query = "UPDATE Requests SET status = '{}', result = '{}' WHERE url = '{}' AND email = '{}';".format(status, result, url, email)
    data = db.execute_query(query)
    db.disconnect()
    print("Data updated successfully")
    return data


def add_record(url, email):
    db.connect()
    query = "INSERT INTO Requests (url, email) VALUES ('{}', '{}')".format(url, email)
    data = db.execute_query(query)
    db.disconnect()
    return data
