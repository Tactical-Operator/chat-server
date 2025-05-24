import requests
import time

SERVER_URL = "https://026cdf88-5881-4b9c-87cb-234163d867ef-00-b5cj60sobzr6.pike.replit.dev:8080/"
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
