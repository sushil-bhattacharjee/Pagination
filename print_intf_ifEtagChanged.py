import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3
from rich import print

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# RESTCONF API Details for IOS-XE
# BASE_URL = "http://10.1.10.99:9280/restconf/data/tailf-ncs:devices/"
# RESOURCE = "device=R1/config/tailf-ned-cisco-ios:interface/GigabitEthernet=2"

# RESTCONF API Details for IOS-XR
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


# Previously saved E-Tag (replace with the actual saved E-Tag)
previous_etag = 'W/"1735-894051-529046+json"'

# Fetch the current resource details
response = requests.get(url, headers=headers, verify=False)

print("Response Headers:")
print(json.dumps(dict(response.headers), indent=4))
print("\n")

if response.status_code == 200:
    # Extract the current E-Tag
    current_etag = response.headers.get("ETag")
    print(f"Current E-Tag: {current_etag}")

    if current_etag == previous_etag:
        print("\n[green]The resource has not changed. E-Tag is still the same.[/green\n]")
    else:
        print("\n[yellow]The resource has changed. Fetching updated details...[/yellow]\n")
        
        # Print the updated interface details
        response_data = response.json()
        print("Updated Interface Details:")
        print(json.dumps(response_data, indent=4))
else:
    print(f"Failed to fetch the resource. HTTP Status Code: {response.status_code}")
    print(f"Error: {response.text}")
