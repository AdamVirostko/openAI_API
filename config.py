import os
import configparser


OPENAI_API_KEY_CONFIG = "API_KEY"


class Config:
# TODO make Config class Singleton

    _instance = None

    def __new__(cls, file_path="./config.ini"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.file_path = file_path
            cls._instance.config = configparser.ConfigParser()

            if os.path.exists(cls._instance.file_path):
                cls._instance.config.read(cls._instance.file_path)
        return cls._instance

    def get(self, section, key):
        if section in self.config:
            if key in self.config[section]:
                return self.config[section][key]
        return None
    
    def set(self, section, key, value):
        if section not in self.config:
            self.config[section] = {}
        self.config[section][key] = value

        with open(self.config, "w") as config_file:
            self.config.write(config_file)
