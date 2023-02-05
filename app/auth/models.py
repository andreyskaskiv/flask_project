from datetime import datetime

from peewee import CharField, IntegerField, DateTimeField, ForeignKeyField

from app.base_model import BaseModel


class Role(BaseModel):
    name = CharField(max_length=100, unique=True, index=True)


class Profile(BaseModel):
    name = CharField(max_length=100)
    old = IntegerField()
    city = CharField(max_length=100)


class User(BaseModel):
    email = CharField(max_length=50, unique=True)
    psw = CharField(max_length=500)
    date = DateTimeField(default=datetime.now())
    role = ForeignKeyField(Role, backref='users')
    profile = ForeignKeyField(Profile)
