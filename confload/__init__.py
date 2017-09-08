from typing import Union

from confload.ini import IniConfig
from confload.json import JsonConfig
from confload.yaml import YamlConfig


class Config:
    _instance: Union[IniConfig, JsonConfig, YamlConfig] = IniConfig

    def __init__(self, file):
        Config.load(file)

    @staticmethod
    def load(file: str):
        if "ini" in file:
            Config._instance = IniConfig
        if "json" in file:
            Config._instance = JsonConfig
        if "yaml" in file:
            Config._instance = YamlConfig

        Config._instance.load(file)

    @staticmethod
    def ready():
        return Config._instance.ready()

    @staticmethod
    def get(section) -> dict:
        return Config._instance.get(section)
