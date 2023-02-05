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
