import requests

class PublicIP:
    def __init__(self, endpoint: str = "https://api.ipify.org") -> None:
        self.endpoint = endpoint

    def get(self) -> str:
        return requests.get(self.endpoint).text