import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-mediControl")
    SQLALCHEMY_DATABASE_URI = "sqlite:///medicontrol.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False