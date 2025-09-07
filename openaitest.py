from openai import OpenAI
from config import apikey

# initialize client
client = OpenAI(api_key=apikey)

# create a text completion
response = client.completions.create(
    model="gpt-3.5-turbo-instruct",  # replacement for text-davinci-003
    prompt="Hello, I am Jarvis AI. How can I help you?",
    max_tokens=100,
    temperature=0.7
)

print(response.choices[0].text.strip())

