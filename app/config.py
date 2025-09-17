import os
from typing import Optional
from dotenv import load_dotenv
load_dotenv() 

class Settings:
    # Application
    APP_NAME: str = os.getenv("PROJECT_NAME", "None")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    HOST: str = os.getenv("HTTP_HOST", "0.0.0.0")
    PORT: int = int(os.getenv("HTTP_PORT", 8080))
    HTTP_EXPOSE_PORT: int = int(os.getenv("HTTP_EXPOSE_PORT", 8000))
    # Concurrency
    MAX_WORKERS: int = int(os.getenv("MAX_WORKERS", 4))
    GRACEFUL_TIMEOUT: int = int(os.getenv("GRACEFUL_TIMEOUT", 4))
    TIMEOUT: int = os.getenv("WORKERS_TIMEOUT", 120)
    KEEPALIVE: int = os.getenv("WORKERS_KEEPALIVE", 5)
    MAX_REQUESTS: int = os.getenv("WORKERS_MAX_REQUESTS", 1000)
    REQUESTS_JITTER : int = os.getenv("WORKERS_REQUESTS_JITTER", 100)
    RELOAD: bool = DEBUG
    #Log
    ACCESSLOG: str = os.getenv("ACCESSLOG", "-")
    ERRORLOG = os.getenv("ERRORLOG", "-")
    LOGLEVEL = os.getenv("LOGLEVEL", "debug")
    #agent LLM
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    MODEL_NAME:str = os.getenv("MODEL_NAME")
    LITELLM_PROVIDER:str = os.getenv("LITELLM_PROVIDER")
    LITELLM_API_KEY:str = os.getenv("LITELLM_API_KEY")
    GOOGLE_APPLICATION_CREDENTIALS:str = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    GOOGLE_API_KEY = GEMINI_API_KEY
    GOOGLE_APPLICATION_CREDENTIALS = GOOGLE_APPLICATION_CREDENTIALS
    # Set Langchain specific environment variables
    LANGCHAIN_API_KEY = GEMINI_API_KEY
    LANGCHAIN_PROVIDER:str = os.getenv("PROVIDER")
    
    # Remove any conflicting environment variables
    OPENAI_API_KEY:str = os.environ.pop("OPENAI_API_KEY", None)
    LITELLM_OPENAI_API_KEY:str = os.environ.pop("LITELLM_OPENAI_API_KEY", None)
    LITELLM_API_KEY:str = os.environ.pop("LITELLM_API_KEY", None)
    LITELLM_PROVIDER:str = os.environ.pop("LITELLM_PROVIDER", None)
    CREWAI_API_KEY:str = os.environ.pop("CREWAI_API_KEY", None)
    CREWAI_PROVIDER:str = os.environ.pop("CREWAI_PROVIDER", None)

settings = Settings()