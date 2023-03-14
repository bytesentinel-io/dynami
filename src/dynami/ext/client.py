import requests
import json

class Client():
    def __init__(self, provider: object) -> None:
        self.provider = provider
        
    def update(self, ip: str) -> None:
        data = json.dumps(self.provider.generate_request(ip=ip))
        result = requests.put(url=self.provider.url,headers=self.provider.headers,data=data)
        return result