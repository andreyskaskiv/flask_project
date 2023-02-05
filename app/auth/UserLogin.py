from flask_login import UserMixin
from app.auth.models import Users


class UserLogin(UserMixin):
    def from_db(self, user_id):
        self.__user = Users.get(Users.id == user_id)
        # self.__user = Users.select().where(Users.id == user_id).first()
        return self

    def create(self, user):
        self.__user = user
        return self

    def get_id(self):
        return str(self.__user.id)

    def get_name(self):
        return self.__user.profile.name if self.__user else "No name"

    def get_email(self):
        return self.__user.email if self.__user else "No email"