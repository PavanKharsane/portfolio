import google.generativeai as genai
from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv("api.env")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

app = FastAPI()

SYSTEM_PROMPT = """
You are an AI assistant for Pavan Kharsane's AWS Cloud Engineer portfolio.
Answer professionally about his AWS, DevOps, SRE, cloud projects, resume analyzer, 
and enterprise OTT cloud platforms.
"""

class Chat(BaseModel):
    message: str

@app.post("/chat")
def chat(req: Chat):
    response = model.generate_content(SYSTEM_PROMPT + "\nUser: " + req.message)
    return {"reply": response.text}
