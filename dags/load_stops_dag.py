import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from scripts.data_upload import load_stops_data_to_db

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'load_stops_dag',
    default_args=default_args,
    description='A DAG to fetch alert data from an API',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

# Define the task
fetch_task = PythonOperator(
    task_id='load_stops_data',
    python_callable= load_stops_data_to_db,
    dag=dag,
)

# Set the task in the DAG
fetch_task