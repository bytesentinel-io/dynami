import requests
import json

class Client():
    def __init__(self, provider: object) -> None:
        self.provider = provider
        
    def set(self, record: str, value: str, type: str) -> None:
        result = None
        try:
            result = self.provider.update_record(value=value, type=type, record=record)
            if result.status_code >= 299:
                raise Exception("Not successful!")
        except Exception as e:
            result = self.provider.create_record(value=value, type=type, record=record)
        return result