This script provides a convenient way to interact with the OpenAI API. It allows you to easily send requests to the OpenAI API and receive responses in return. It also provides a simple interface for sending and receiving data, making it easy to use with minimal setup. With this script, you can quickly and easily send requests to the OpenAI API and receive responses, allowing you to quickly and efficiently use the OpenAI API.

# Installation

In order to use the openai prompting script, you will need to have Python 3 installed. After installing Python 3, you must install openai library, you can do this by running the following command:

`pip install openai`

Once openai is installed, you need to set up your API key. To set up your API key you can run following command:

`python3 main.py --api=<API_KEY>`

This will set up your API key in config.ini.

You can also set your API key by rewriting manually config.ini among other configuration settings. However, recommended way of setting configuration settings is by running the command.
For more, run:

`python3 main.py --help`

or

`python3 main.py -h`

# Usage

To prompt OpenAI, run this command

`python3 main.py --prompt=<PROMPT>`

where `<PROMPT>` is the prompt you wish to use. The script will then generate a response based on the given prompt. 

You can combine sending a prompt and setting multiple settings in one command. This allows you to apply new settings and prompting OpenAI more easily.

Example:

`python3 main.py --prompt="What is the meaning of life?" --temperature=0.9 --tokens=200`

This will set new values for temperature and token parameters. Then prompt will be sent with already applied settings. 
After receiving a response from OpenAI, it will be stored response.txt file by default, or in other user specified file. Result will be written in response file followingly:

\# Beginning of the file

Prompt:
What is the meaning of life?

Response:

The meaning of life is subjective and can mean different things to different people. Ultimately, it is up to each individual to decide what meaningful life looks like for them.

\---

\# Other prompts