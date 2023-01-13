from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Resume Parser API | CareerMunzil"
    affinda_token: str
    azure_account_name: str
    azure_primary_key: str
    azure_container: str
    azure_sas_expiry: int

    class Config:
        env_file = ".env"

settings = Settings()