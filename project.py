import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key = api_key
)

chat_completion = client.chat.completions.create(
    messages = [
        {
            "role": "user",
            "content": "What team won nba finals 2012",
        }
    ],
    model = "gpt-3.5-turbo"
)

print(chat_completion.choices[0].message.content)