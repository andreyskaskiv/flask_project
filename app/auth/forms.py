from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[Email("Некоректний email")])
    psw = PasswordField("Password: ", validators=[DataRequired(),
                                                Length(min=4, max=100,
                                                       message="Пароль має бути від 4 до 100 символів")])
    remember = BooleanField("Remember me", default=False)
    submit = SubmitField("To come in")


class RegisterForm(FlaskForm):
    name = StringField("Имя: ", validators=[Length(min=4, max=100, message="Ім'я має бути від 4 до 100 символів")])
    old = StringField("Вік: ", validators=[Length(min=1, max=3, message="Вік має бути від 1 до 3 символів")])
    city = StringField("Місто: ", validators=[Length(min=2, max=100, message="Місто має бути від 2 до 100 символів")])
    email = StringField("Email: ", validators=[Email("Некорректный email")])
    psw = PasswordField("Пароль: ", validators=[DataRequired(),
                                                Length(min=4, max=100,
                                                       message="Пароль має бути від 4 до 100 символів")])

    psw2 = PasswordField("Повтор пароля: ", validators=[DataRequired(), EqualTo('psw', message="Паролі не співпадають")])
    submit = SubmitField("Реєстрація")
