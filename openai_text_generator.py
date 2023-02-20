import argparse
from open_ai_manager import ApiKey, OpenAI, ResponseStore
from config import Config


class InputManager:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Interact with OpenAI API")
        self.parser.add_argument("prompt", type=str, help="")
        self.parser.add_argument("--temperature", type=float, default=0.5, help="")
        self.parser.add_argument("--tokens", type=self.check_positive_integer, default=1000, help="")

    def parse_args(self):
        return self.parser.parse_args()
    
    def check_positive_integer(self, value):
        positive_value = int(value)
        if positive_value <= 0:
            raise argparse.ArgumentTypeError("Token must be a positive integer.")
        return value
    

if __name__ == "__main__":
    config = Config()
    api_key = ApiKey(config.get("openai", "API_KEY"))
    if api_key is None:
        config.set("openai", "API_KEY", "ExZKIMzczy0BaLDJWPRX")
        
    input_manager = InputManager()
    args = input_manager.parse_args()
    print("Prompt: ", args.prompt)
    print("temperature: ", args.temperature)
    print("token: ", args.tokens)
    
    openai = OpenAI(api_key)
    response = openai.send_prompt(args.prompt, args.tokens, args.temperature)
    response_store = ResponseStore()
    response_store.save_response(response)
    response_store.load_response()
