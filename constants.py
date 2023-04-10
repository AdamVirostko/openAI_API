

class Constants:
    TOKENS_UPPER_BOUND = 2048

    TOKENS_LOWER_BOUND = 1
    
    TEMPERATURE_LOWER_BOUND = 0.0
    
    TEMPERATURE_UPPER_BOUND = 1.0
    
    CONFIG_FILE_PATH = "config.ini"
    
    OPENAI_SECTION = "OPENAI"
    
    CONFIG_DEFAULTS = {
    "TEMPERATURE": "0.5",
    "TOKENS": "1000",
    "MODEL": "text-davinci-003",
    "RESPONSE_FILE": "response.txt",
    }

    ALLOWED_MODELS = [
        "text-davinci-003",
        "text-davinci-002",
    ]
    
    RESPONSE_FILE_KEY = "RESPONSE_FILE"

    TOKENS_PARAMETER = "TOKENS"

    TEMPERATURE_PARAMETER = "TEMPERATURE"

    API_KEY_PARAMETER = "API_KEY"

    MODEL_PARAMETER = "MODEL"

    OPEN_AI_BILLING_OVERVIEW_URL = "https://platform.openai.com/account/billing/overview"