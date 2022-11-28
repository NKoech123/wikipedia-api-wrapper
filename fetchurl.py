import requests
import json

def fetch_api(url: str) -> any:
    headers = {'User-Agent' : 'GrtLit' }
    try:
        response_api = requests.get(url, headers=headers)
        data = response_api.text
    except KeyError as e:
        print(e)
    parse_json = json.loads(data)
    return parse_json