from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def get_response( message: str):
    if not message:
        message = "Calculate the sum of exponentials of first 3 Fibonacci numbers"
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=message,
    )
    return response.text
