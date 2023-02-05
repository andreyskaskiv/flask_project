from flask import render_template, request, redirect, flash, url_for
from flask_login import login_required, LoginManager, logout_user, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash

from app.auth import auth
from app.auth.UserLogin import UserLogin
from app.auth.forms import LoginForm, RegisterForm
from app.auth.models import Users, Profiles
from app.main_menu import menu

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = "Авторизуйтесь для доступу до закритих сторінок"
login_manager.login_message_category = "success"


@login_manager.user_loader
def load_user(user_id):
    return UserLogin().from_db(user_id)


@auth.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.profile'))

    form = LoginForm()
    if form.validate_on_submit():
        user = Users.select().where(Users.email == form.email.data).first()
        if user and check_password_hash(user.psw, form.psw.data):
            userlogin = UserLogin().create(user)
            remember_me = form.remember.data
            login_user(userlogin, remember=remember_me)
            return redirect(request.args.get("next") or url_for("auth.profile"))

        flash("Невірна пара логін/пароль", "error")

    title = "Login"
    return render_template("login.html",
                           title=title,
                           menu=menu,
                           form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Ви вийшли з облікового запису", "success")
    return redirect(url_for('auth.login'))


@auth.route('/profile')
@login_required
def profile():
    title = "Profile"
    return render_template("profile.html",
                           title=title,
                           menu=menu)


@auth.route("/register", methods=("POST", "GET"))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if not Users.select().where(Users.email == form.email.data).first():
            try:
                profile = Profiles(name=form.name.data,
                                   old=form.old.data,
                                   city=form.city.data)
                profile.save()
                hash_psw = generate_password_hash(form.psw.data)
                user = Users(email=form.email.data,
                             psw=hash_psw,
                             profile=profile.id)
                user.save()
            except:
                print("Помилка додавання до БД")

            flash("Ви успішно зареєстровані", "success")
            return redirect(url_for('auth.login'))

        flash(f"User with this {form.email.data} already exists")

    title = "Registration"
    return render_template("register.html",
                           title=title,
                           menu=menu,
                           form=form)
