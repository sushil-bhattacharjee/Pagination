import requests
import json

url = "https://api.discogs.com/artists/1/releases?page=2&per_page=35"

# Send the GET request
response = requests.get(url)

# Extract the headers
headers = response.headers

# Convert headers to a dictionary
headers_dict = dict(headers)

# Pretty-print the headers as JSON
print("Headers in JSON Format:")
print(json.dumps(headers_dict, indent=4))

#Extract the JSON response body
try:
    response_body = response.json()
    print("\nResponse Body in JSON Format:")
    print(json.dumps(response_body, indent=4))
except json.JSONDecodeError:
    print("\nResponse body is not in JSON format!")
    
    
# Navigate to the pagination section and extract 'urls'
pagination = response_body.get("pagination", {})
urls = pagination.get("urls", {})
# Find the next page url
if urls:
    print("\nPagination URLs in JSON Format:")
    print(json.dumps(urls, indent=4))
    
    # Check the and extract the 'next' URL
    next_url = urls.get("next")
    if next_url:
        print(f"\nNEXT URL: {next_url}")
    else:
        print("\nNo 'next' URL found.")
        
else:
    print("\nNo pagination URLs found.")
    
