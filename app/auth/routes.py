from flask import render_template, request, redirect, flash, url_for
from flask_login import login_required, LoginManager, logout_user, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash

from app.auth import auth
from app.auth.UserLogin import UserLogin
from app.auth.models import Users, Profiles
from app.main_menu import menu

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"
login_manager.login_message_category = "success"


@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return UserLogin().from_db(user_id)


@auth.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.profile'))

    if request.method == "POST":
        user = Users.select().where(Users.email == request.form['email']).first()
        if user and check_password_hash(user.psw, request.form['psw']):
            userlogin = UserLogin().create(user)
            remember_me = True if request.form.get("remainme") else False
            login_user(userlogin, remember=remember_me)
            return redirect(request.args.get("next") or url_for("auth.profile"))

        flash("Неверная пара логин/пароль", "error")
    title = "Login"
    return render_template("login.html",
                           title=title, menu=menu)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Вы вышли из аккаунта", "success")
    return redirect(url_for('auth.login'))


@auth.route('/profile')
@login_required
def profile():
    return f"""<a href="{url_for('auth.logout')}">Выйти из профиля</a>
                user info: {current_user.get_id()} """


@auth.route("/register", methods=("POST", "GET"))
def register():
    if request.method == "POST":

        # add wtforms and CSRF
        if len(request.form['name']) > 4 and len(request.form['email']) > 4 \
                and len(request.form['psw']) > 4 and request.form['psw'] == request.form['psw2']:

            if not Users.select().where(Users.email == request.form['email']).first():
                try:
                    profile = Profiles(name=request.form['name'],
                                       old=request.form['old'],
                                       city=request.form['city'])
                    profile.save()
                    hash_psw = generate_password_hash(request.form['psw'])
                    user = Users(email=request.form['email'],
                                 psw=hash_psw,
                                 profile=profile.id)
                    user.save()
                except:
                    print("Ошибка добавления в БД")

                flash("Вы успешно зарегистрированы", "success")
                return redirect(url_for('auth.login'))
            flash(f"User with this {request.form['email']} already exists")
        else:
            flash("Неверно заполнены поля", "error")

    title = "Registration"
    return render_template("register.html",
                           title=title,
                           menu=menu)
