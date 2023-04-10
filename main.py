from open_ai import OpenAI
from response_store import ResponseStore
from input_manager import InputManager


args = InputManager().parse_args()

prompt = args.prompt
openai = OpenAI(args.tokens, args.temperature, args.api, args.model)
response_store = ResponseStore(args.filename)

if prompt:
    response = openai.send_prompt(prompt)
    print(response)
    response_store.save_response(prompt, response)
