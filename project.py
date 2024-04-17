import os
from openai import OpenAI

client = OpenAI(
    api_key = "sk-proj-5AnjLnqzLJeOnQuL4yfXT3BlbkFJTq3DUIwpSIVt6kKbqK0z"
)

chat_completion = client.chat.completions.create(
    messages = [
        {
            "role": "user",
            "content": "ßWhat team won nba finals 2012",
        }
    ],
    model = "gpt-3.5-turbo"
)

print(chat_completion.choices[0].message.content)