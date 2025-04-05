from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_ID: int
    API_HASH: str
    SESSION_NAME: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
