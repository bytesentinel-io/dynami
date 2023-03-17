import requests
import json
from enumy import Enumy

class Hetzner:
    def __init__(self, api_key: str, zone: str) -> None:
        self.headers = {
            "Auth-API-Token": api_key,
            "Content-Type": "application/json"
        }
        self.record_type = Enumy(("A", "AAAA", "CNAME", "TXT", "NS", "RP", "SOA", "HINFO", "SRV", "DANE", "DS", "CAA", "TLSA"), str)
        self.zone_id = self.get_zone_id(zone=zone)

    def create_record(self, value: str, type: str, record: str) -> dict:
        self.record_type.set(type)
        url = "https://dns.hetzner.com/api/v1/records"
        data = json.dumps({
            "value": value,
            "ttl": 86400,
            "type": str(self.record_type),
            "name": record,
            "zone_id": self.zone_id
        })
        result = requests.post(url, headers=self.headers, data=data)
        return result

    def update_record(self, value: str, type: str, record: str) -> dict:
        self.record_type.set(type)
        record_id = self.get_record_id(record=record)
        url = "https://dns.hetzner.com/api/v1/records/" + record
        data = json.dumps({
            "value": value,
            "ttl": 86400,
            "type": str(self.record_type),
            "name": record,
            "zone_id": self.zone_id
        })
        result = requests.put(url, headers=self.headers, data=data)
        return result

    def get_zone_id(self, zone: str) -> str:
        url = "https://dns.hetzner.com/api/v1/zones"
        zones = requests.get(url, headers=self.headers).json()
        for z in zones["zones"]:
            if z["name"] == zone:
                return z["id"]

    def get_record_id(self, record: str) -> str:   
        url = "https://dns.hetzner.com/api/v1/records"
        params = {
            "zone_id": self.zone_id
        }
        records = requests.get(url, headers=self.headers, params=params).json()
        for r in records["records"]:
            if r["name"] == record:
                return r["id"]

    def __generate_request(self, value: str = "0.0.0.0", type: str = "A") -> dict:
        self.record_type.set(type)
        data = {
            "value": value,
            "type": str(self.record_type),
            "name": self.record,
            "zone_id": self.zone_id
        }
        return data