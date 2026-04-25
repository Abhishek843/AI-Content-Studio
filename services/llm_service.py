import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY", "AIzaSyAPTdiELSprSm8f76WK3uu7Ug3Twv42yvM"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_text(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text.strip()