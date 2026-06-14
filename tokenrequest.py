#!/usr/bin/env python
import requests
import sys

# Replace with your actual credentials
client_id = '103408'
client_secret = 'ev9nFH32UDYFJ7WvCTHnenNheSyi2bWy'

def get_token():
    url = "https://www.gwn.cloud/oauth/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        token = response.json().get("access_token")
        print("? Connected to GWN Cloud API.")
        print(f"Access Token: {token}")
        return token
    except requests.RequestException as e:
        print("? Failed to connect to GWN Cloud API:")
        print(e)

# Run test
get_token()
