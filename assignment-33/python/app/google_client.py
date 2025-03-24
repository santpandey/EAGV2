from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
print(api_key)
client = genai.Client(api_key=api_key)


def get_response():
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Calculate the sum of exponentials of first 3 Fibonacci numbers",
    )
    return response.text
