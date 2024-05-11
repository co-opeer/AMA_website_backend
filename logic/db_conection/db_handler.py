import mysql.connector


class MySQLDatabase:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            database=self.database
        )
        if self.connection.is_connected():
            print("Connected to MySQL database")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Disconnected from MySQL database")

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def fetch_data(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        return records



