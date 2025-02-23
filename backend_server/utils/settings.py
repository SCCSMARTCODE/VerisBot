import os


class Settings:
    apikey: str = os.getenv("HF_API_KEY")
    api_url: str = os.getenv("HF_API_URL")


settings = Settings()