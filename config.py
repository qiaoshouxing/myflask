import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    STATIC_FOLDER = 'assets'
    STATIC_URL_PATH = '/assets'
    DEBUG = True

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}