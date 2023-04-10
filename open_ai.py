from config import Config
from constants import Constants
from messages import Messages
import openai


class OpenAI:
    def __init__(self, tokens=None, temperature=None, api_key=None, model=None):
        self.tokens = int(self.get_parameter_value(Constants.TOKENS_PARAMETER, tokens))
        self.temperature = float(self.get_parameter_value(Constants.TEMPERATURE_PARAMETER, temperature))
        self.api_key = self.get_parameter_value(Constants.API_KEY_PARAMETER, api_key)
        self.model = self.get_parameter_value(Constants.MODEL_PARAMETER, model)
        if not self.api_key:
            raise TypeError(Messages.API_KEY_NOT_FOUND)

    def set_to_config(self, parameter, value):
        """Sets value in config."""
        config = Config()
        config.set(Constants.OPENAI_SECTION, parameter, str(value))

    def get_from_config(self, parameter):
        """Return a value from config."""
        config = Config()
        return config.get("OPENAI", parameter)

    def get_parameter_value(self, parameter_name, value):
        if value:
            self.set_to_config(parameter_name, value) 
            return value
        return self.get_from_config(parameter_name)

    def send_prompt(self, prompt):
        """Return Open AI response as a string
        Sends prompt to Open AI API
        """
        
        openai.api_key = self.api_key
        response = openai.Completion.create(
            model=self.model, 
            prompt=prompt, 
            temperature=self.temperature, 
            max_tokens=self.tokens
            )    
        try:
            return response["choices"][0]["text"]
        except openai.error.RateLimitError:
            print(Messages.OPEN_AI_QUOTA_EXCEEDED.format(Constants.OPEN_AI_BILLING_OVERVIEW_URL))
