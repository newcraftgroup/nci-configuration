import json

from confload import IniConfig


class JsonConfig:
    data = {}

    @staticmethod
    def load(file: str):
        with open(file, 'r') as jsonfile:
            JsonConfig.data = json.load(jsonfile)

    @staticmethod
    def ready() -> bool:
        return len(IniConfig.parser.sections()) > 0

    @staticmethod
    def get(section) -> dict:
        return JsonConfig.data[section]