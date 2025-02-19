from database.db_connector import DatabaseConnector
import json
import os
import env
import glob
import hashlib
import shutil
def get_newest_file(directory):
    # Get a list of all files in the directory
    list_of_files = glob.glob(os.path.join(directory, '*'))
    # Find the newest file based on modification time
    newest_file = max(list_of_files, key=os.path.getmtime, default = 0)
    return newest_file

def move_file_to_processed(file_path, processed_directory):
    try:
        # Ensure the processed directory exists
        os.makedirs(processed_directory, exist_ok=True)
        # Move the file to the processed directory
        destination_path = os.path.join(processed_directory, os.path.basename(file_path))
        shutil.move(file_path, destination_path)
        print(f"Moved {file_path} to {destination_path}")
    except Exception as e:
        print(f"Error moving file: {e}")

def calculate_md5(file_path):
    # Initialize the MD5 hash object
    hash_md5 = hashlib.md5()
    # Read the file in binary mode and update the hash object
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def compare_md5(file1, file2):
    # Calculate MD5 checksums for both files
    if not file1 or not file2:
        return False
    md5_file1 = calculate_md5(file1)
    md5_file2 = calculate_md5(file2)
    # Compare the checksums
    return md5_file1 == md5_file2

def load_json_to_db(json_file_path, table_name):
    # Read JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Connect to the database
    connection = DatabaseConnector()
    connection.connect()

    # Extract values from the JSON data
    columns = data["data"][table_name][0].keys()
    values = [tuple(row.values()) for row in data["data"][table_name]]
    query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES {', '.join([str(val) for val in values])} ON CONFLICT (id) DO NOTHING"
    # Insert data into the database
    connection.execute_query(query, params=None)
    connection.commit()

    # Close the connection
    connection.close()
    print(f"Data loaded into {table_name} successfully!")

def load_stops_data_to_db():
    newest_raw = get_newest_file(f"{env.DATA_PATH}/raw/stops")
    newest_processed = get_newest_file(f"{env.DATA_PATH}/processed/stops")
    # Don't do anything if the contents of the files are the same
    """
    if compare_md5(newest_raw, newest_processed):
        return
    """
    # iterate over files in that directory
    for root, dirs, files in os.walk(f"{env.DATA_PATH}/raw/stops/"):
        for filename in files:
            file_path = os.path.join(root, filename)
            load_json_to_db(file_path, "stops")
            move_file_to_processed(file_path, f"{env.DATA_PATH}/processed/stops")
