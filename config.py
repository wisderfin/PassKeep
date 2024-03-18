from pydantic_settings import BaseSettings


class SettingsDB(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    class Config:
        env_file = '.env'


settings_db = SettingsDB()