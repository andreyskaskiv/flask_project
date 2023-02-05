from flask import Flask

from peewee import SqliteDatabase

from app.auth.routes import login_manager
from app.base_model import database_proxy
from app.config import config


def create_app(config_name='default'):
    app = Flask(__name__)
    app.static_folder = 'static'
    app.config.from_object(config[config_name])

    db = SqliteDatabase(app.config['DB_NAME'], pragmas={'foreign_keys': 'on'})
    database_proxy.initialize(db)
    app.config['db'] = db

    login_manager.init_app(app)

    from app.main import main
    from app.auth import auth
    from app.about import about


    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(about)

    return app
