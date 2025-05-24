import requests

SERVER_URL = "/"


print (" Relay Server Sender")
while True:
    message = input("Enter your message (or 'exit'): ")
    if message.lower() == "exit":
        break
    payload = {"sender": "Sender", "message": message}
    response = requests.post(f"{SERVER_URL}/send", json=payload)
    print("Server:", response.json())
