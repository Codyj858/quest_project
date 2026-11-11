import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    if not JWT_SECRET_KEY:
        raise RuntimeError("JWT_SECRET_KEY environment variable is required")
    INTERNAL_SERVICE_TOKEN = os.environ.get("INTERNAL_SERVICE_TOKEN")
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 60
    DATABASE_URL = os.getenv("DATABASE_URL")

class DevelopmentConfig(Config):
    DEBUG = os.getenv("FLASK_DEBUG", "1") == "1"
    SQLALCHEMY_DATABASE_URI = Config.DATABASE_URL or "sqlite:///dev.db"

class TestingConfig(Config):
    TESTING = os.getenv("FLASK_TESTING", "1") == "1"
    SQLALCHEMY_DATABASE_URI = "sqlite:///test_dev.db"

class ProductionConfig(Config):
    DEBUG = os.getenv("FLASK_DEBUG", "1") == "1"
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"