import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3
from rich import print

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Headers for the request
headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic YWRtaW46YWRtaW4=',
}

# Make the GET request
# response = requests.get('http://10.1.10.99:9280/restconf/data/tailf-ncs:devices/device=R1', headers=headers, verify=False)
#response_Gi2 = http://10.1.10.99:9280/restconf/data/tailf-ncs:devices/device=R1/config/tailf-ned-cisco-ios:interface/GigabitEthernet=2
# response_snmp = requests.get('http://10.1.10.99:9280/restconf/data/tailf-ncs:devices/device=R1/config/tailf-ned-cisco-ios:snmp-server', headers=headers, verify=False)
# Print the response to console
# print(response.text)
#print(response_snmp.text)
# Print response headers
# print("Response Headers:")
# print(json.dumps(dict(response.headers), indent=4))

# # Save the response to a JSON file
# try:
#     # Parse response as JSON
#     response_data = response.json()
    
#     # Save JSON data to file
#     with open('response_output.json', 'w') as file:
#         json.dump(response_data, file, indent=4)
#         print("[green]Response saved to 'response_output.json'[/green]")
# except ValueError:
#     # Handle cases where response is not valid JSON
#     with open('response_output.json', 'w') as file:
#         file.write(response.text)
#         print("[yellow]Response saved as plain text to 'response_output.json'[/yellow]")


# RESTCONF API Details
BASE_URL = "http://10.1.10.99:9280/restconf/data/tailf-ncs:devices/device=R1/config/"
RESOURCE = "tailf-ned-cisco-ios:interface/GigabitEthernet=2"


# Build the URL
url = f"{BASE_URL}/{RESOURCE}"

# Send the GET request
response = requests.get(
    url,
    headers=headers,
    verify=False  # Disable SSL verification (not recommended for production)
)

# Print response headers
# print("Response Headers:")
# print(response.headers)
# Check if the request was successful
if response.status_code == 200:
    # Extract the E-Tag from the response headers
    etag = response.headers.get("ETag")
    print(f"E-Tag: {etag}")
    
    # Print the response body
    response_data = response.json()
    print("Response Data:")
    print(json.dumps(response_data, indent=4))
else:
    print(f"Failed to fetch the resource. HTTP Status Code: {response.status_code}")
    print(f"Error: {response.text}")

