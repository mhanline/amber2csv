#!/usr/bin/env python3

from time import sleep
import requests
import csv
from datetime import datetime, timezone
siteID = "" #Your unique Amber Site ID
apiKey = "" #Your API key from Amber: https://app.amber.com.au/developers/

if __name__ == '__main__':
    sleep(3)
    headers = {
        'Authorization': f"Bearer {apiKey}",
        'accept': 'application/json'
    }
    nowtime = datetime.now().astimezone().replace(microsecond=0)
    response = requests.get(f"https://api.amber.com.au/v1/sites/{apiKey}/prices/current", headers=headers)
    if response.status_code==200:
        data = response.json()
        for item in data:
            with open(f"amber-prices-{item['channelType']}.csv", "a+", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([nowtime, datetime.fromisoformat(item['startTime']).astimezone(), item['perKwh'], item['estimate']])
                print(f"Log: {[str(nowtime), str(datetime.fromisoformat(item['startTime']).astimezone()), item['perKwh'], item['estimate'] ]}")
    else:
        print(f"Error: {response.status_code}, {response.text}")
