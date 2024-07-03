import logging
from datetime import datetime, timedelta

import requests
import tomli

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - line:%(lineno)d - %(filename)s:%(funcName)s -> %(message)s",
)

# with open("/app/src/config.toml", mode="rb") as config_file:
#     config = tomli.load(config_file)
with open("./config.toml", mode="rb") as config_file:
    config = tomli.load(config_file)

# Get today's date
today = datetime.now().date()
yesterday = today - timedelta(days=1)


def get_sleep():
    url = "https://api.ouraring.com/v2/usercollection/sleep"
    headers = {"Authorization": f"Bearer {config['oura']['token']}"}
    params = {"start_date": f"{yesterday}", "end_date": f"{today}"}
    response = requests.request("GET", url, headers=headers, params=params)

    if response.status_code == 200:
        logging.info("Successfully retrieved sleep data")

    return response.text


def get_stress():
    url = "https://api.ouraring.com/v2/usercollection/daily_stress"
    headers = {"Authorization": f"Bearer {config['oura']['token']}"}
    params = {"start_date": f"{yesterday}", "end_date": f"{yesterday}"}
    response = requests.request("GET", url, headers=headers, params=params)

    if response.status_code == 200:
        logging.info("Successfully retrieved stress data")

    return response.text


def get_blood_oxygen():
    url = "https://api.ouraring.com/v2/usercollection/daily_spo2"
    headers = {"Authorization": f"Bearer {config['oura']['token']}"}
    params = {"start_date": f"{yesterday}", "end_date": f"{yesterday}"}
    response = requests.request("GET", url, headers=headers, params=params)

    if response.status_code == 200:
        logging.info("Successfully retrieved blood o2 data")

    return response.text


def get_activity():
    url = "https://api.ouraring.com/v2/usercollection/daily_activity"
    headers = {"Authorization": f"Bearer {config['oura']['token']}"}
    params = {"start_date": f"{yesterday}", "end_date": f"{today}"}
    response = requests.request("GET", url, headers=headers, params=params)

    if response.status_code == 200:
        logging.info("Successfully retrieved activity data")

    return response.text
