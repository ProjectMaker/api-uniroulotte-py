import os
from dotenv import load_dotenv

load_dotenv(verbose=True)


class BaseConfig(object):
    ORIGINS = ['*']
    MONGO_URL = os.getenv("MONGO_URL")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")


class Development(BaseConfig):
    DEBUG = True
    PORT = 5000


config = {
    'development': 'config.Development'
}


def get_config():
    return config[os.getenv('FLASK_ENV')]
