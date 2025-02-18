import env
from scripts.graphql_queries import *
from env import API_URL, API_KEY
import requests
from datetime import datetime
import json
import os


def get_stops_data():
    body = stop_data_query()
    os.makedirs("data/raw/stops", exist_ok=True)
    response = requests.post(url=API_URL, json={"query": body},
                             headers={"digitransit-subscription-key": API_KEY})
    data = json.loads(response.content)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f'{env.DATA_PATH}/raw/stops/stops_{timestamp}.json', 'w') as f:
        json.dump(data, f)

def get_alert_data():
    os.makedirs("data/raw/alerts", exist_ok=True)
    body = distruptions_query()
    response = requests.post(url=API_URL, json={"query": body},
                             headers={"digitransit-subscription-key": API_KEY})
    data = json.loads(response.content)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f'{env.DATA_PATH}/raw/alerts/alerts_{timestamp}.json', 'w') as f:
        json.dump(data, f)

def get_canceled_trip_data():
    page = 1
    next_page = True
    after = None
    while next_page:
        body = cancelled_trips_query(after = after)
        os.makedirs("data/raw/cancelled_trips", exist_ok=True)
        response = requests.post(url=API_URL, json={"query": body},
                                 headers={"digitransit-subscription-key": API_KEY})
        data = json.loads(response.content)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open(f'{env.DATA_PATH}/raw/cancelled_trips/cancelled_trip_{timestamp}-{page}.json', 'w') as f:
            json.dump(data, f)
        next_page = data["data"]["canceledTrips"]["pageInfo"]["hasNextPage"]
        after = data["data"]["canceledTrips"]["pageInfo"]["endCursor"]

if __name__=="__main__":
    get_alert_data()