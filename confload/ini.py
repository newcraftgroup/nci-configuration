import configparser

from confload import Config


class IniConfig:
    parser = configparser.ConfigParser()

    @staticmethod
    def load(file: str):
        Config.parser = configparser.ConfigParser()
        Config.parser.read(file)

    @staticmethod
    def ready() -> bool:
        return len(IniConfig.parser.sections()) > 0

    @staticmethod
    def get(section) -> dict:
        dict1 = {}
        options = IniConfig.parser.options(section)
        for option in options:
            try:
                dict1[option] = IniConfig.parser.get(section, option)
                if dict1[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1