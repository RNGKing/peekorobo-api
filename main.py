from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "hello world!"}
