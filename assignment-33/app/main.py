from fastapi import FastAPI
from client.google_client import get_response
#from google import genai
app = FastAPI()


@app.get("/get_llm_response/{message}")
def read_root(message: str):
    return get_response(message)    