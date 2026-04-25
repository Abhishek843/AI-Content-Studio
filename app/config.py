import os

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyAPTdiELSprSm8f76WK3uu7Ug3Twv42yvM")
    MODEL_NAME = "gemini-1.5-flash"  # fast + free tier

settings = Settings()