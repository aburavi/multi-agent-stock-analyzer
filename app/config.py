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
    #Gemini LLM
    GEMINI_API_KEY: str = os.getenv("GG_GEMINI_API_KEY")
    GEMINI_MODEL_NAME:str = os.getenv("GG_MODEL_NAME")
    GEMINI_LITELLM_PROVIDER:str = os.getenv("GG_LITELLM_PROVIDER")
    GEMINI_LITELLM_API_KEY:str = os.getenv("GG_LITELLM_API_KEY")
    GOOGLE_APPLICATION_CREDENTIALS:str = os.getenv("GG_GOOGLE_APPLICATION_CREDENTIALS")
    GOOGLE_API_KEY = GEMINI_API_KEY
    # Set Langchain specific environment variables
    GOOGLE_LANGCHAIN_API_KEY = GEMINI_API_KEY
    GOOGLE_LANGCHAIN_PROVIDER:str = os.getenv("GG_PROVIDER")
    
    #Huggingface LLM
    HUGGINGFACE_API_KEY: str = os.getenv("HG_API_KEY")
    HUGGINGFACE_MODEL_NAME:str = os.getenv("HG_MODEL_NAME")
    HUGGINGFACE_LITELLM_PROVIDER:str = os.getenv("HG_LITELLM_PROVIDER")
    HUGGINGFACE_LITELLM_API_KEY:str = os.getenv("HG_LITELLM_API_KEY")
    
    HUGGINGFACE_LANGCHAIN_API_KEY = HUGGINGFACE_API_KEY
    HUGGINGFACE_LANGCHAIN_PROVIDER:str = os.getenv("HG_PROVIDER")
    
    #Qwen LLM
    QWEN_BASE_URL: str = os.getenv("QW_BASE_URL")
    QWEN_API_KEY: str = os.getenv("QW_API_KEY")
    QWEN_MODEL_NAME:str = os.getenv("QW_MODEL_NAME")
    QWEN_LITELLM_PROVIDER:str = os.getenv("QW_LITELLM_PROVIDER")
    QWEN_LITELLM_API_KEY:str = os.getenv("QW_LITELLM_API_KEY")
    
    QWEN_LANGCHAIN_API_KEY = QWEN_API_KEY
    QWEN_LANGCHAIN_PROVIDER:str = os.getenv("QW_PROVIDER")
    
    # Remove any conflicting environment variables
    OPENAI_API_KEY:str = os.environ.pop("OA_API_KEY", None)
    OPENAI_LITELLM_OPENAI_API_KEY:str = os.environ.pop("OA_LITELLM_OPENAI_API_KEY", None)
    OPENAI_LITELLM_API_KEY:str = os.environ.pop("OA_LITELLM_API_KEY", None)
    OPENAI_LITELLM_PROVIDER:str = os.environ.pop("OA_LITELLM_PROVIDER", None)
    
    # crewAI
    CREWAI_API_KEY:str = os.environ.pop("CREWAI_API_KEY", None)
    CREWAI_PROVIDER:str = os.environ.pop("CREWAI_PROVIDER", None)


    os.environ["PROJECT_ID"] = "API Project"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS
    os.environ["DASHSCOPE_API_KEY"] = QWEN_API_KEY
    os.environ["OPENAI_API_KEY"] = QWEN_API_KEY
    
settings = Settings()