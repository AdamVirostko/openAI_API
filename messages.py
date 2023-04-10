

class Messages:
    DESCRIPTION = "Interact with OpenAI API"

    PROMPT_HELP = "Ask OpenAI. Wrap your question in single or double quotes"

    TEMPERATURE_HELP = "Temperature parameter in OpenAI API is a hyperparameter used to adjust the creativity of the generated text, with higher values leading to more creative, unexpected output. You can set temperature by \npython3 --temperature=<TEMPERATURE>. \nTemperature must be in range of 0.0 to 1.0, default value is 0.5."

    TEMPERATURE_OUT_OF_RANGE = "Temperature must be of float type in range {} to {}."

    TOKENS_HELP = "Parameter tokens is a parameter specifies the maximum number of tokens that can be returned in a single API call. You can set max_tokens by \npython3 --tokens=<TOKENS>. \nTokens must be in range of 0 to 2048, default value is 1000."

    TOKENS_OUT_OF_RANGE = "Tokens value must be of integer type in range {} to {}."

    API_KEY_HELP = "API key is a unique identifier used to authenticate requests to the OpenAI API. API key must be set in config.ini. You can set your API key by \npython3 --api=<API_KEY>."

    API_KEY_NOT_FOUND = "API key not found. Please set your API key with: \n\tpython3 --api=<API_KEY>."

    MODEL_HELP = "Model parameters are the variables used to define the architecture and behavior of a machine learning model. They are typically used to control the complexity of the model and the properties of the output. In OpenAI API, model parameters are used to specify the architecture and hyperparameters of the model, such as the number of layers, the learning rate, and the optimizer. You can set model by \npython3 --model=<MODEL>. \nDefault model is text-davinci-003."

    MODEL_INVALID_MESSAGE = "Provided model is not valid or allowed. Please choose from following models: {}."

    FILENAME_HELP = "Response filename can be set to store OpenAI responses. You can set different response filename by \npython3 <prompt> --filename=<filename>. \nDefault response filename is response.txt."

    FILENAME_INVALID_MESSAGE = "File name contains invalid character."

    OPEN_AI_QUOTA_EXCEEDED = "You exceeded your current quota. Please check your plan and billing details at {}."

