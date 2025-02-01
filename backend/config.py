import os

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-api-key")
    MONGO_URI = os.getenv("MONGO_URI", "your-mongo-uri")


