from config import Config
from constants import Constants


class ResponseStore:
    def __init__(self, filename=None):
        if filename:
            self.filename = filename
            self.set_filename_to_config(filename) 
        else:
            self.filename = self.get_filename_from_config()

    def set_filename_to_config(self, filename):
        config = Config()
        config.set(Constants.OPENAI_SECTION, Constants.RESPONSE_FILE_KEY, filename)

    def get_filename_from_config(self):
        config = Config()
        return config.get(Constants.OPENAI_SECTION, Constants.RESPONSE_FILE_KEY)

    def save_response(self, prompt, response):
        with open(self.filename, "a") as file:
            file.write(f"\nPrompt:\n{prompt}\n")
            file.write(f"\nResponse:{response}\n")
            file.write("\n---\n")

    def load_response(self):
        with open(self.filename, "r") as file:
            for line in file:
                print(line)
