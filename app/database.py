from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DataBase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

"""
from web import app
from app.database import db
with app.app_context():
    db.create_all()
"""


class Navigation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<navigation {self.id}>"


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    profiles = db.relationship('Profiles', backref='users', uselist=False)

    def __repr__(self):
        return f"<users {self.id}>"


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    old = db.Column(db.Integer)
    city = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<profiles {self.id}>"


class ReadDataBase:
    def get_navigation(self):
        try:
            menu = Navigation.query.all()
            if menu: return menu
        except:
            print("Ошибка чтения из БД")
        return []

    def get_users(self):
        try:
            info = Users.query.all()
            if info: return info
        except:
            print("Ошибка чтения из БД")
        return []

    def check_email(self, email):
        try:
            if Users.query.filter(Users.email == email).all():
                return True
        except:
            print("Ошибка чтения из БД")
        return False

    # def check_user(self, user_id):
    #     try:
    #         if Users.query.filter(Users.id == user_id).all(): # возвращает записи с конкретным id
    #             return True
    #         print("Пользователь не найден")
    #         return False
    #     except:
    #         print("Ошибка чтения из БД")

    def get_user_by_id(self, user_id):
        try:
            user_by_id = Users.query.filter(Users.id == user_id).all()  # возвращает записи с конкретным id
            if not user_by_id:
                print("Пользователь не найден")
                return False
            return user_by_id
        except:
            print("Ошибка чтения из БД")
        return False

    def get_user_by_email(self, email):
        try:
            user_by_email = Users.query.filter_by(email=email).all()  # возвращает все записи с таким email=email
            if not user_by_email:
                print("Пользователь не найден")
                return False
            return user_by_email
        except:
            print("Ошибка чтения из БД")
        return False
