import requests
import json

def fetch_api(url: str) -> any:
    headers = {'User-Agent' : 'GrtLit' }
    response_api = requests.get(url, headers=headers)
    data = response_api.text
    parse_json = json.loads(data)

    return parse_json