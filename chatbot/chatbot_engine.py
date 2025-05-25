import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

def get_medical_response(user_query):
    if not API_KEY:
        return "API key not found. Please set it in the .env file."

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a concise medical assistant. Provide brief, accurate, and relevant medical answers only. Do not add extra explanations or greetings."
            },
            {"role": "user", "content": user_query}
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        answer = response.json()["choices"][0]["message"]["content"]
        return answer.strip()
    except Exception as e:
        print("Error in API call:", e)
        return "Sorry, I couldn't get an answer right now. Please try again later."
