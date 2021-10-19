import os

from sqlalchemy.sql.elements import False_

"""
Модуль с описанием конфигурации для REST-сервера Flask
"""
POSTS_PER_PAGE = 1
class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog.db"
    SECRET_KEY = 'secret-key-goes-here'
    TESTING = False
    LOGIN_DISABLED = False
    UPLOAD_FOLDER = "./app/static/pic"
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


    USER_ENABLE_EMAIL = False  # хз
    USER_ENABLE_USERNAME = False  # хз
    USER_ENABLE_AUTH0 = False  # хз
    USER_UNAUTHENTICATED_ENDPOINT = "login"  # хз
    USER_UNAUTHORIZED_ENDPOINT = "login"  # хз