import requests
import os
import config as Config


OPENAI_API_KEY_ENV = "OPENAI_API_KEY"


class ApiKey:
    def __init__(self, api_key=None):
        if api_key is not None:
            self.api_key = api_key
        else: 
            self.api_key = self.fetch_from_config()
    
    def fetch_from_config(self):
        config = Config()
        api_key = self.config.get("openai", "api_key")
        if api_key is None:
            raise ValueError("API key not found in config")
        self.api_key = api_key
        return None


class OpenAI:
    def __init__(self, api_key) -> None:
        self.api_key = ApiKey(api_key).api_key
        self.api_endpoint = "https://api.openai.com/v1/engines/text-davinci-002/jobs"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

    def send_prompt(self, prompt, tokens=1000, temperature=0.5):
        payload = {
            "prompt": prompt,
            "max_tokens": tokens,
            "temperature": temperature
        }

        response = requests.post(self.api_endpoint, headers=self.headers, json=payload)
        
        if response != 200:
            raise Exception("Failed to send a prompt")

        response_json = response.json()
        generated_text = response_json["choices"][0]["text"]
        return generated_text


class ResponseStore:
    def __init__(self, filename="response.txt"):
        self.filename = filename

    def save_response(self, prompt, response):
        with open(self.filename, "w") as file:
            file.write(f"Prompt:\n{prompt}\nResponse:\n{response}\n")

    def load_response(self):
        with open(self.filename, "r") as file:
            for line in file:
                print(line)
        return None        
    