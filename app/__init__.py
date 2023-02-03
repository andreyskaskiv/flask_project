from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import config


def create_app(config_name='default'):
    app = Flask(__name__)
    app.static_folder = 'static'
    app.config.from_object(config[config_name])



    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DataBase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    app.config['db'] = db

    from app.main import main
    from app.auth import auth
    from app.about import about

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(about)

    return app


