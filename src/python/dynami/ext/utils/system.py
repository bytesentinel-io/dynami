import os
import sys

class OSInspector:
    def __init__(self, choice: dict) -> None:
        self.os = self.get_os()
        self.__choice = choice

    def __call__(self) -> None:
        return self.__choice[self.os]

    def get_os(self) -> None:
        match os.name:
            case "nt":
                return "windows"
            case "posix":
                if sys.platform == "darwin":
                    return "mac"
                elif sys.platform.startswith("linux"):
                    return "linux"
                else:
                    return None
                

if __name__ == "__main__":
    inspector = OSInspector({
        "mac": print
    })
    inspector(inspector.os)