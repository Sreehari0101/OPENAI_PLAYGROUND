from openai import OpenAI
from dotenv import load_dotenv

client = OpenAI(load_dotenv.get("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a chatbot."},
        {"role": "user", "content": "What is the capital of the United States?"}
    ]
)

print(response.choices[0].message.content)
