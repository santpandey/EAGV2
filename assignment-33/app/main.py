from fastapi import FastAPI
from client.google_client import get_response
#from google import genai
app = FastAPI()


@app.get("/message2/")
def read_root():
    return get_response()    