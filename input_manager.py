import argparse
from constants import Constants
from messages import Messages
import re


class InputManager:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description=Messages.DESCRIPTION)
        self.parser.add_argument("--prompt", type=str, help=Messages.PROMPT_HELP)
        self.parser.add_argument("--temperature", type=self.check_if_temperature_valid, default=0.5, help=Messages.TEMPERATURE_HELP)
        self.parser.add_argument("--tokens", type=self.check_if_tokens_valid, default=1000, help=Messages.TOKENS_HELP)
        self.parser.add_argument("--api", type=str, help=Messages.API_KEY_HELP)
        self.parser.add_argument("--model", type=self.check_if_model_valid, help=Messages.MODEL_HELP)
        self.parser.add_argument("--filename", type=self.check_if_valid_filename, default="response.txt", help=Messages.FILENAME_HELP)

    def parse_args(self):
        return self.parser.parse_args()
    
    def check_if_model_valid(self, value):
        model = str(value)
        if model not in Constants.ALLOWED_MODELS:
            raise argparse.ArgumentTypeError(Messages.MODEL_INVALID_MESSAGE.format(', '.join(Constants.ALLOWED_MODELS)))
        return model

    def check_if_valid_filename(self, filename):
        valid_filename_pattern = re.compile(r'^[\w.]+\.([aA-zZ0-9]+)$')
        if not valid_filename_pattern.match(filename):
            raise argparse.ArgumentTypeError(Messages.FILENAME_INVALID_MESSAGE)
        return filename

    def check_if_temperature_valid(self, value):
        temperature = float(value)
        if not Constants.TEMPERATURE_LOWER_BOUND <= temperature <= Constants.TEMPERATURE_UPPER_BOUND:
            raise argparse.ArgumentTypeError(Messages.TEMPERATURE_OUT_OF_RANGE.format(Constants.TEMPERATURE_LOWER_BOUND, Constants.TEMPERATURE_UPPER_BOUND))
        return temperature

    def check_if_tokens_valid(self, value):
        tokens = int(value)
        if not Constants.TOKENS_LOWER_BOUND <= tokens <= Constants.TOKENS_UPPER_BOUND:
            raise argparse.ArgumentTypeError(Messages.TOKENS_OUT_OF_RANGE.format(Constants.TOKENS_LOWER_BOUND, Constants.TOKENS_UPPER_BOUND))
        return value
    
