import configparser
from generic.fileFunctionUtil import FileFunctionUtil


class ReadconfigProperty:
    @staticmethod
    def get_config_data(key):
        try:
            config = configparser.RawConfigParser()
            config.read(FileFunctionUtil.get_dynamic_path("DemoBlazePOC") + "\\configuration\\config.ini")
            if key != "":
                value = config.get("Application Info", key)
                return value
        except Exception as exp:
            print(f"I'm getting exception {exp.__class__} while fetching config file data.")
            return " "
