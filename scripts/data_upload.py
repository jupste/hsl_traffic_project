from database.db_connector import DatabaseConnector
import json

def load_json_to_db(json_file_path, table_name):
    # Read JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Connect to the database
    connection = DatabaseConnector()
    connection.connect()

    # Prepare the SQL query for insertion
    columns = data[0].keys()
    query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES %s ON CONFLICT (id) DO NOTHING"


    # Extract values from the JSON data
    values = [tuple(row.values()) for row in data]

    # Insert data into the database
    connection.execute_query(query, params=None)
    connection.commit()

    # Close the connection
    connection.close()
    print(f"Data loaded into {table_name} successfully!")