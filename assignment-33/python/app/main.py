from fastapi import FastAPI
from client.google_client import get_response
from google import genai
app = FastAPI()


@app.get("/message")
def read_root():
    client = genai.Client(api_key="AIzaSyAhhxxYBbP3SEIhQj-TF_dMNKlPeiG_kHk")
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Calculate the sum of exponentials of first 3 Fibonacci numbers",
    )
    print(response.text)

    return response.text

@app.get("/message2/")
def read_root():
    return get_response()    