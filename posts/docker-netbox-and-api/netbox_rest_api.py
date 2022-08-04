import requests
from pprint import pprint

headers = {
    'Authorization': 'Token 0123456789abcdef0123456789abcdef01234567',
    'Content-Type': 'application/json',
}

netbox_api_url = 'http://0.0.0.0:8000/api'

full_url = netbox_api_url + '/dcim/manufacturers/'

payload = {
    'name': 'Fortinet'
}

r = requests.get(full_url, headers=headers, params=payload)

# .json () provides the API's response in JSON format ; .txt in clear text
pprint(r.json())