import json
import requests

class Discover:

    def __init__(self,discovery_url="https://discovery.meethue.com"):
        self.discovery_url = discovery_url

    def find_hue_bridge(self):
        response = requests.get(self.discovery_url, verify=False)

        result = response.json()
        if result and type(result) is list and "error" in result[0] and result[0]["error"]:
            raise Exception(result[0]["error"]["description"])        

        return json.dumps(result, indent=4)
