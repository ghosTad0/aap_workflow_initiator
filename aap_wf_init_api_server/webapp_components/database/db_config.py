from urllib.parse import quote_plus
import os
from aap_wf_init_api_server.commons.configurator import flask_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from aap_wf_init_api_server.commons.configurator import config
from aap_wf_init_api_server.commons.configurator import base_dir


class Base(DeclarativeBase):
  pass


class DBConfig(object):
    SECRET_KEY = config.get('sqlalchemy', 'SECRET_KEY')
    db_engine = config.get('sqlalchemy', 'DB_ENGINE')
    db_name = config.get('sqlalchemy', 'DB_NAME')
    db_host = config.get('sqlalchemy', 'DB_HOST')
    db_user = config.get('sqlalchemy', 'DB_USER')
    db_pass = config.get('sqlalchemy', 'DB_PASS')
    db_port = config.get('sqlalchemy', 'DB_PORT') if config.get('sqlalchemy', 'DB_PORT') else 3306

    if db_engine == 'sqlite':
        db_file_name = 'db/' + db_name + '.sqlite'
        SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(base_dir, db_file_name)
        SQLALCHEMY_TRACK_MODIFICATIONS = False  # Avoids SQLAlchemy warning
        SQLALCHEMY_ECHO = True

    if db_engine == 'mariadb' or db_engine == 'mysql':
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{db_user}:{quote_plus(db_pass)}@{db_host}:{db_port}/{db_name}"
        SQLALCHEMY_TRACK_MODIFICATIONS = False  # Avoids SQLAlchemy warning
        SQLALCHEMY_ECHO = False
        SQLALCHEMY_ENGINE_OPTIONS = {
            'pool_size': int(config.get('sqlalchemy', 'pool_size')),
            'pool_recycle': int(config.get('sqlalchemy', 'pool_recycle')),
            'pool_pre_ping': True
        }



flask_app.config.from_object(DBConfig)

# Create the SqlAlchemy db instance
db = SQLAlchemy(app=flask_app, model_class=Base)
