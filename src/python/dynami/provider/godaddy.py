import requests
import json
from enumy import Enumy

class GoDaddy:
    def __init__(self, api_key: str, zone: str) -> None:
        self.headers = {
            "Authorization": "sso-key " + api_key,
            "Content-Type": "application/json"
        }
        self.record_type = Enumy(("A", "AAAA"), str)
        self.zone_id = zone

    def create_record(self, value: str, type: str, record: str) -> requests.Response:
        self.record_type.set(type)
        url = "https://api.godaddy.com/v1/domains/" + self.zone_id + "/records/" + str(self.record_type) + "/" + record
        data = json.dumps([{
            "data": value,
            "name": record,
            "ttl": 600
        }])
        result = requests.put(url, headers=self.headers, data=data)
        return result

    def update_record(self, value: str, type: str, record: str) -> requests.Response:
        self.record_type.set(type)
        url = "https://api.godaddy.com/v1/domains/" + self.zone_id + "/records/" + str(self.record_type) + "/" + record
        data = json.dumps({
            "data": value,
            "name": record,
            "ttl": 600
        })
        result = requests.put(url, headers=self.headers, data=data)
        return result