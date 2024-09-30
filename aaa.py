import requests
import json
import os

api_key = os.environ["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"]
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Assuming the updated endpoint expects a list of messages
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "This is a test."}
    ]
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(data))
if response.status_code == 200:
    print("API Key is valid. Response received successfully.")
else:
    print(f"Failed to validate API Key: HTTP {response.status_code} - {response.text}")