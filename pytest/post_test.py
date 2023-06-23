import requests
import json

url = "http://localhost:8000/api/v1/student/auth/register"  # Replace with your endpoint URL

# Create the JSON payload
payload = {
    "name": "achu",
    "regNo": "21bce0000",
    "block": "C",
    "password": "asdfasdf",
    "roomNo": "1347",
}

# payload = {"regNo": "21bce0000", "password": "asdfasdf"}

# Send the POST request
response = requests.post(url, json=payload)

# Check the response status code
if response.status_code == 200:
    print(response.json())
else:
    print(response)
