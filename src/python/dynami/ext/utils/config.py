import json

class ConfigControl:
    def __init__(self, path: str) -> None:
        self.config_path = path

    def read(self) -> None:
        self.config = json.load(open(self.config_path, "r"))

    def save(self, value: dict = None) -> None:
        if value is None:
            with open(self.config_path, "w") as f:
                f.write(json.dumps(self.config))
                f.close()
        else:
            with open(self.config_path, "w") as f:
                f.write(json.dumps(value))
                f.close()

    def set(self, attribute: str, value: str) -> dict:
        self.config[attribute] = value
        return self.config[attribute]