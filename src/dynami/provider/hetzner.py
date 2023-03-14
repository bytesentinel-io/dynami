import requests

class Hetzner:
    def __init__(self, api_key: str, zone: str, record: str) -> None:
        self.headers = {
            "Auth-API-Token": api_key,
            "Content-Type": "application/json"
        }
        self.zone = zone
        self.record = record
        self.zone_id = self.get_zone_id()
        self.record_id = self.get_record_id()
        self.url = "https://dns.hetzner.com/api/v1/records/" + self.record_id

    def get_zone_id(self) -> str:
        url = "https://dns.hetzner.com/api/v1/zones"
        zones = requests.get(url, headers=self.headers).json()
        for zone in zones["zones"]:
            if zone["name"] == self.zone:
                return zone["id"]

    def get_record_id(self) -> str:   
        url = "https://dns.hetzner.com/api/v1/records"
        params = {
            "zone_id": self.zone_id
        }
        records = requests.get(url, headers=self.headers, params=params).json()
        for record in records["records"]:
            if record["name"] == self.record:
                return record["id"]

    def generate_request(self, ip: str = "0.0.0.0") -> dict:
        data = {
            "value": ip,
            "type": "A",
            "name": self.record,
            "zone_id": self.zone_id
        }
        return data