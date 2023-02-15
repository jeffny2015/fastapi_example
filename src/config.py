from pydantic import BaseSettings
from functools import lru_cache

class AuthSettings(BaseSettings):
    API_KEY: str
    
    class Config:
        env_file = ".env.sample"
        
class DbSettings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    
    class Config:
        env_file = ".env.sample"
        
class APICatSettings(BaseSettings):
    API_URI: str
    
    class Config:
        env_file = ".env.sample"
        env_prefix = "CAT_"

@lru_cache()
def get_auth_settings():
    return AuthSettings()

@lru_cache()
def get_db_settings():
    return DbSettings()

@lru_cache()
def get_cat_settings():
    return APICatSettings()

db_settings = get_db_settings()
    