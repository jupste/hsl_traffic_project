# Airflow Data Pipeline Project
This project demonstrates a data pipeline built using Apache Airflow to fetch, process, and store data from a traffic API. The pipeline includes tasks for data ingestion, cleaning, transformation, and storage.

## Project Overview
### Objective
The goal of this project is to:

Fetch traffic data (e.g., cancelled trips, disruption info, and stops) from an external API.

Process and clean the data.

Store the processed data in a database.

Visualize the data using a dashboard.

### Project Structure
```
airflow-traffic-pipeline/
├── dags/                   # Airflow DAG files
│   └── traffic_pipeline.py
├── scripts/                # Python scripts for tasks
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   └── data_storage.py
├── data/                   # Data storage
│   ├── raw/                # Raw data from the API
│   └── processed/          # Processed data
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```
## Setup Instructions
### 1. Prerequisites

- ***Python 3.8+***

- ***Apache Airflow 2.0+***

### 2. Install Dependencies

1. Clone this repository:
```
git clone https://github.com/jupste/hsl-traffic-project.git
cd hsl-traffic-project
```

2. Install the required Python packages:

```pip install -r requirements.txt ```
3. Configure Airflow and initialize the Airflow database:

```
airflow db init
```
4. Create an Airflow user:
```
airflow users create \
    --username admin \
    --firstname YourName \
    --lastname YourLastName \
    --role Admin \
    --email your_email@example.com
```
Update the dags_folder in airflow.cfg to point to the dags directory in this project:
```
dags_folder = /path/to/airflow-traffic-pipeline/dags
```
5. Start the Airflow webserver and scheduler:
```
airflow webserver --port 8080
airflow scheduler
```
6. Access the Airflow UI at http://localhost:8080.

## Running the Pipeline
Place your DAG files in the dags directory.

Ensure your Python scripts are in the scripts directory.

Trigger the DAG manually from the Airflow UI or wait for it to run based on the schedule.

### DAG Details
The pipeline consists of the following tasks:

***Fetch Data:*** Fetches traffic data from the API.

***Clean Data:*** Cleans and preprocesses the raw data.

***Store Data:*** Stores the processed data in a database.

### Data Storage
***Raw Data:*** Stored in data/raw/.

***Processed Data:*** Stored in data/processed/.

### Visualization

TBD

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements.

### License
This project is licensed under the MIT License. See the LICENSE file for details.
