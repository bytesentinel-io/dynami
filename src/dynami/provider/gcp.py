import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.cloud import dns

import json

class GoogleCloud:
    def __init__(self, credentials: str, project: str, zone: str) -> None:
        # Read service account credentials file
        self.credentials = service_account.Credentials.from_service_account_file(credentials)
        self.client = dns.Client(project=project, credentials=self.credentials)
        self.zone = self.client.zone(zone)

    def create_record(self, value: str, type: str, record: str) -> dict:
        data = {
            "rdtype": type,
            "rdata": value,
            "ttl": 86400
        }
        new_record = self.zone.resource_record_set(name=record, record_type=type)
        new_record.add_rdata(data)
        new_record.create()
        return new_record
    
    def delete_record(self, record: str, type: str) -> dict:
        existing_record = self.zone.resource_record_set(name=record, type=type)
        existing_record.delete()
        return existing_record

    def update_record(self, value: str, type: str, record: str) -> dict:
        data = {
            "rdtype": type,
            "rdata": value,
            "ttl": 86400
        }
        existing_record = self.zone.resource_record_set(name=record, record_type=type)
        existing_record.delete()
        new_record = self.zone.resource_record_set(name=record, record_type=type)
        new_record.add_rdata(data)
        new_record.create()
        return new_record