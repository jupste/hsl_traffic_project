from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from scripts.data_ingestion import get_stops_data

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
    'fetch_alerts_dag',
    default_args=default_args,
    description='A DAG to fetch alert data from an API',
    schedule_interval=timedelta(hours=1),
    catchup=False,
)

# Define the task
fetch_task = PythonOperator(
    task_id='fetch_alert_data',
    python_callable= get_stops_data,
    dag=dag,
)

# Set the task in the DAG
fetch_task