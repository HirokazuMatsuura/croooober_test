import requests
import json
import time
from datetime import datetime

def put_request(url, request_id):
    response = requests.put(url, headers={"X-Challenge-Id": request_id})
    return json.loads(response.text)

def update_value(array):
    return (array["actives_at"] / 1000), array["total_diff"]

url = 'http://challenge.z2o.cloud/challenges?nickname=hoge'

response = requests.post(url)
text = json.loads(response.text)
request_id = text["id"]
actives_at = text["actives_at"] / 1000
total_diff = text["total_diff"]

url = 'http://challenge.z2o.cloud/challenges'
print(response.text)
    
while total_diff <= 500:
    time_diff = actives_at - time.time() - 0.001
    time.sleep(time_diff)
    req = put_request(url, request_id)
    print(req)
    if "result" in req:
        exit()
    actives_at, total_diff = update_value(req)