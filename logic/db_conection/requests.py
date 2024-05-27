# Параметри для підключення до бази даних MySQL
import os

from logic.db_conection.db_handler import MySQLDatabase


# Отримання даних з файлу JSON
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
    return data


def add_record(url, email):
    db.connect()
    query = "INSERT INTO Requests (url, email) VALUES ('{}', '{}')".format(url, email)
    data = db.execute_query(query)
    db.disconnect()
    return data
