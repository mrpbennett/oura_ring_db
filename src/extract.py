from datetime import datetime, timedelta

import requests
import tomli

with open("/app/src/config.toml", mode="rb") as config_file:
    config = tomli.load(config_file)

# Get today's date
today = datetime.today().date()

# Calculate the date for the previous day
yesterday = today - timedelta(days=1)


def get_sleep():
    url = "https://api.ouraring.com/v2/usercollection/sleep"
    headers = {"Authorization": f"Bearer {config['oura']['token']}"}
    params = {"start_date": f"{yesterday}", "end_date": f"{today}"}
    response = requests.request("GET", url, headers=headers, params=params)
    return response.text


def get_stress():
    url = "https://api.ouraring.com/v2/usercollection/daily_stress"
    headers = {"Authorization": f"Bearer {config['oura']['token']}"}
    params = {"start_date": f"{today}", "end_date": f"{today}"}
    response = requests.request("GET", url, headers=headers, params=params)
    return response.text


def get_blood_oxygen():
    url = "https://api.ouraring.com/v2/usercollection/daily_spo2"
    headers = {"Authorization": f"Bearer {config['oura']['token']}"}
    params = {"start_date": f"{today}", "end_date": f"{today}"}
    response = requests.request("GET", url, headers=headers, params=params)
    return response.text


def get_activity():
    url = "https://api.ouraring.com/v2/usercollection/daily_activity"
    headers = {"Authorization": f"Bearer {config['oura']['token']}"}
    params = {"start_date": f"{yesterday}", "end_date": f"{today}"}
    response = requests.request("GET", url, headers=headers, params=params)
    return response.text
