import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    PROJECT_NAME: str = "Test Blog"
    PROJECT_VERSION: str = "1.0.0"

    DB_URL: str = os.getenv("POSTGRES_URL")


settings = Settings()
