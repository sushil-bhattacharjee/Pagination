###Using APIs Q6###
import requests
import argparse
import json
from rich import print


BASE_URL = "https://api.meraki.com/api/v1/organizations"
DEVICES_URL = "https://api.meraki.com/api/v1/organizations/1215707/devices"
API_KEY = "75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6"
params = {"perPage": 3}
headers = {"Authorization": f"Bearer {API_KEY}", "Accept": "application/json"}
res = requests.get(DEVICES_URL, headers=headers, params=params)
#print(res.text.encode('utf8'))
#print(res.json())

formatted_message = """
Meraki Dashboard API Response
--------------------------------
Response Status Code : {}
Response Link Header : {}
Response Body : {}
""".format(res.status_code, res.headers.get('Link'), json.dumps(res.json(), indent=4))

print(formatted_message)
res_headers = json.dumps(dict(res.headers), indent=4)
print("\n[blue]Response Headers:\n", res_headers)

# Retrieve the next page of results
next_page_url = res.links['next']['url']
print(f"\n[yellow][bold]Next page URL: [/yellow][/bold]{next_page_url}")
next_page_response = requests.get(next_page_url, headers=headers)
print("\n[yellow][bold]Next Page Response:\n", json.dumps(next_page_response.json(), indent=4))