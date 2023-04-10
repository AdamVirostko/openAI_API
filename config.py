import os
import configparser
from constants import Constants


class Config:

    _instance = None

    def __new__(cls, file_path=Constants.CONFIG_FILE_PATH):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.file_path = file_path
            cls._instance.config = configparser.ConfigParser()

            if os.path.exists(cls._instance.file_path):
                cls._instance.config.read(cls._instance.file_path) # check
            else:
                cls._instance.create_config()
        return cls._instance

    def get(self, section, key):
        """Return a string value from a config file"""
        if section in self.config and key in self.config[section]:
            return self.config[section][key]
    
    def set(self, section, key, value):
        """Sets value in config file."""
        if section not in self.config:
            self.config[section] = {}
        self.config[section][key] = value

        with open(self.file_path, "w") as config_file:
            self.config.write(config_file)

    def create_config(self):
        """Creates config file and sets default values in config file."""
        os.system(self.file_path)
        if not self.config.has_section(Constants.OPENAI_SECTION):
            self.config.add_section(Constants.OPENAI_SECTION)
        for default_setting in Constants.CONFIG_DEFAULTS.keys():
            self.set(Constants.OPENAI_SECTION, default_setting, Constants.CONFIG_DEFAULTS[default_setting])
    