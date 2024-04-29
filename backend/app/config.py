


class Config(object):
    DEBUG = False
    SITE_NAME = 'Flask Application'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///todo.db'


class ProductionConfig(Config):
    DEBUG = False
    # Here we can use a real database like MySQL, PostgreSQL, Oracle, etc.
    # SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/todo'

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    


