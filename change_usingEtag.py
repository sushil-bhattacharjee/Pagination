import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3
from rich import print

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# RESTCONF API Details for IOS-XE
# BASE_URL = "http://10.1.10.99:9280/restconf/data/tailf-ncs:devices/device=R1/config/"
# RESOURCE = "tailf-ned-cisco-ios:interface/GigabitEthernet=2"

#RESTCONF API Details for IOS-XR
BASE_URL = "http://10.1.10.99:9280/restconf/data/tailf-ncs:devices/"
RESOURCE = "device=xr-sandbox/config/tailf-ned-cisco-ios-xr:interface/GigabitEthernet=0%2F0%2F0%2F0"

# Build the URL
url = f"{BASE_URL}/{RESOURCE}"

# Headers for the request
headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic YWRtaW46YWRtaW4=',
}

# Fetch the current configuration to retrieve the E-Tag
response = requests.get(url, headers=headers, verify=False)

if response.status_code == 200:
    # Extract the E-Tag
    etag = response.headers.get("ETag")
    print(f"E-Tag: {etag}")

    # Prepare the payload to update the interface description for IOS-XE
    # payload = {
    #     "tailf-ned-cisco-ios:GigabitEthernet": [
    #         {
    #             "name": "2",
    #             "description": "Updated via RESTCONF to TEST E-Tag validation",  # New description
    #         }
    #     ]
    # }
    # Prepare the payload to update the interface description for IOS-XE
    payload = {
        "tailf-ned-cisco-ios-xr:GigabitEthernet": [
            {
                "id": "0/0/0/0",
                "description": "Updated via RESTCONF using Cisco NSO",  # New description
            }
        ]
    }

    # Perform the conditional PUT request with the E-Tag
    put_response = requests.patch(
        url,
        headers={
            **headers,
            "If-Match": etag  # Use E-Tag for conditional update
        },
        json=payload,
        verify=False
    )

    # Check the response
    if put_response.status_code == 204:
        print("Interface description updated successfully.")
    elif put_response.status_code == 412:
        print("Precondition Failed: The resource has been modified by someone else.")
    else:
        print(f"Failed to update the resource. HTTP Status Code: {put_response.status_code}")
        print(f"Error: {put_response.text}")
else:
    print(f"Failed to fetch the resource. HTTP Status Code: {response.status_code}")
    print(f"Error: {response.text}")
