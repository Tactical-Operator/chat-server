import requests
import time

SERVER_URL = ""
seen = set()

while True:
    response = requests.get(f"{SERVER_URL}/receive")
    messages = response.json()
    for msg in messages:
        key = (msg['sender'], msg['message'])
        if key not in seen:
            print(f"{msg['sender']}: {msg['message']}")
            seen.add(key)
    time.sleep(2)  # Poll every 2 seconds
