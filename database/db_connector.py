import psycopg2
from psycopg2 import sql
from env import DB_PARAMS

class DatabaseConnector:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(**DB_PARAMS)
            print("Connected to the database!")
        except Exception as error:
            print(f"Error connecting to the database: {error}")

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            cursor.close()
        except Exception as error:
            print(f"Error executing query: {error}")

    def fetch_data(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as error:
            print(f"Error fetching data: {error}")

    def commit(self):
        if self.connection:
            self.connection.commit()
            print("Data committed!")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
