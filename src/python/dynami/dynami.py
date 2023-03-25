import argparse
import os
import json
from pathlib import Path

# Create a tool to use dynami as a command line tool
# ConfigControl is a class to manage the config file
from provider import *
from ext.client import Client
from ext.utils import PublicIP

available_providers = [
    "hetzner",
    "gcp"
]

available_record_types = [
    "A",
    "AAAA",
    "CNAME",
    "MX",
    "NS",
    "TXT",
    "SRV"
]

class DynamiCLI:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__base = Path("~/.dynami").expanduser()
        self.check_config_path()
        self.__config_path = Path(f"{self.__base}/config/{self.__name}.json").expanduser()

    def check_config_path(self) -> None:
        # If path is not existing, create it
        path_list = ["config", "cache"]
        __path = Path(self.__base).expanduser()
        if not os.path.exists(__path):
            os.mkdir(__path)
            print("✅ Created config path!")
        for path in path_list:
            __path = Path(f"{self.__base}/{path}").expanduser()
            if not os.path.exists(__path):
                os.mkdir(__path)

    def set_attr_config(self, attribute: str, value: str) -> dict:
        pass

    def create_config(self, provider: str) -> dict:
        config = {}
        config["name"] = self.__name
        config["provider"] = provider
        if config["provider"] not in available_providers:
            raise Exception("❌ Provider not available!")
        key_type = input("Key: ")
        # Check if key is a path
        config["key"] = {}
        if os.path.exists(key_type):
            config["key"]["type"] = "file"
        else:
            config["key"]["type"] = "token"
        config["key"]["value"] = key_type
        config["domain"] = input("Domain: ")
        config["type"] = input("Type: ")
        if config["type"] not in available_record_types:
            raise Exception("❌ Record type not available!")
        self.__config = config
        
    def delete_config(self) -> None:
        if os.path.exists(self.__config_path):
            os.remove(self.__config_path)
            print("✅ Config successfully deleted!")
        else:
            print("❌ Config not found!")

    def save(self) -> None:
        with open(self.__config_path, "w") as f:
            f.write(json.dumps(self.__config))
            f.close()
        print(f"✅ Config successfully saved! You can find it under ~/.dynami/config/{self.__name}.json")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(title="Configuration", description="Configuration options", dest="sub")

    # Record
    record_parser = sub.add_parser("record", help="Manage records")
    record_sub = record_parser.add_subparsers(title="Record", description="Record options", dest="record_parser")

    # Record: Create
    record_create = record_sub.add_parser("create", help="Create a new record")
    record_create_group = record_create.add_argument_group("record_create")
    record_create_group.add_argument("-n", "--name", help="Name of configuration", type=str, dest="config", metavar="CONFIG", default="default")
    record_create_group.add_argument("-r", "--record", help="Record name", type=str, dest="record_name", default="@", metavar="RECORD")
    record_create_group.add_argument("-t", "--type", help="Record type", type=str, dest="record_type", choices=available_record_types, default="A", metavar="TYPE")
    record_create_group.add_argument("-v", "--value", help="Record value", type=str, dest="record_value", default=None, metavar="VALUE")

    # Config
    config_parser = sub.add_parser("config", help="Manage records")
    config_sub = config_parser.add_subparsers(title="Configuration", description="Configuration options", dest="config_parser")

    # Config: Create
    config_create = config_sub.add_parser("create", help="Create a new configuration")
    config_create_group = config_create.add_argument_group("config_create")
    config_create_group.add_argument("-n", "--name", help="Name of the configuration", type=str, metavar="CONFIG", dest="config", default="default")
    config_create_group.add_argument("-p", "--provider", help="DNS Provider", type=str, metavar="PROVIDER", dest="provider", choices=available_providers)

    # Config: Delete
    config_delete = config_sub.add_parser("delete", help="Delete a configuration")
    config_delete_group = config_delete.add_argument_group("config_delete")
    config_delete_group.add_argument("-n", "--name", help="Name of the configuration", type=str, metavar="CONFIG", dest="config")

    # Config: Set attribute
    config_set = config_sub.add_parser("set", help="Set an attribute of a configuration")
    config_set_group = config_set.add_argument_group("config_set")
    config_set_group.add_argument("-n", "--name", help="Name of the configuration", type=str, metavar="CONFIG", dest="config")
    config_set_group.add_argument("-a", "--attribute", help="Attribute to set", type=str, metavar="ATTRIBUTE", dest="config_set_attribute")
    config_set_group.add_argument("-v", "--value", help="Value to set", type=str, metavar="VALUE", dest="config_set_value")

    args = parser.parse_args()

    cli = DynamiCLI(args.config)

    match args.sub:
        case "record":
            match args.record_parser:
                case "create":
                    print("record", "create", args.record_config, args.record_name, args.record_type, args.record_value)
        case "config":
            match args.config_parser:
                case "create":
                    cli.create_config(provider=args.provider)
                    cli.save()
                case "delete":
                    cli.delete_config()
                case "set":
                    print("config", "set", args.config, args.config_set_attribute, args.config_set_value)