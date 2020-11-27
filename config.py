import settings

class Config(object):

    SQLALCHEMY_DATABASE_URI = f'postgresql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_DBNAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False