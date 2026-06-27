from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str
    redis_url: str
    risk_threshold_block: int
    risk_threshold_review: int

    class Config:
        env_file = ".env"


settings = Settings()
