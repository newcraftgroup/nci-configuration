import yaml


class YamlConfig:
    data = {}

    @staticmethod
    def load(file: str):
        with open(file, 'r') as ymlfile:
            YamlConfig.data = yaml.load(ymlfile)

    @staticmethod
    def ready() -> bool:
        return len(YamlConfig.data) > 0

    @staticmethod
    def get(section) -> dict:
        return YamlConfig.data[section]
