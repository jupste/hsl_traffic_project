from graphql_queries import *
from env import API_URL, API_KEY
import requests
import datetime
import json
import os
def get_stops_data():
    body = stop_data_query()
    os.makedirs("data/raw/stops", exist_ok=True)
    response = requests.post(url=API_URL, json={"query": body},
                             headers={"digitransit-subscription-key": API_KEY})
    data = json.loads(response.content)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f'data/raw/stops/stops_{timestamp}.json', 'w') as f:
        json.dump(data, f)

def get_alert_data():
    body = distruptions_query()
    os.makedirs("data/raw/alerts", exist_ok=True)
    response = requests.post(url=API_URL, json={"query": body},
                             headers={"digitransit-subscription-key": API_KEY})
    data = json.loads(response.content)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f'data/raw/alerts/alerts_{timestamp}.json', 'w') as f:
        json.dump(data, f)

def get_canceled_trip_data():
    body = cancelled_trips_query()
    os.makedirs("data/raw/cancelled_trips", exist_ok=True)
    response = requests.post(url=API_URL, json={"query": body},
                             headers={"digitransit-subscription-key": API_KEY})
    data = json.loads(response.content)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f'data/raw/cancelled_trips/cancelled_trip_{timestamp}.json', 'w') as f:
        json.dump(data, f)