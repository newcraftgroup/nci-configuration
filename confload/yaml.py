import yaml

from confload import IniConfig


class YamlConfig:
    data = {}

    @staticmethod
    def load(file: str):
        with open(file, 'r') as ymlfile:
            YamlConfig.data = yaml.load(ymlfile)

    @staticmethod
    def ready() -> bool:
        return len(IniConfig.parser.sections()) > 0

    @staticmethod
    def get(section) -> dict:
        return YamlConfig.data[section]