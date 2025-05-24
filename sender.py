import requests

SERVER_URL = "https://026cdf88-5881-4b9c-87cb-234163d867ef-00-b5cj60sobzr6.pike.replit.dev:8080/"


print (" Relay Server Sender")
while True:
    message = input("Enter your message (or 'exit'): ")
    if message.lower() == "exit":
        break
    payload = {"sender": "Sender", "message": message}
    response = requests.post(f"{SERVER_URL}/send", json=payload)
    print("Server:", response.json())
