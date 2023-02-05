from flask import render_template, request, redirect, flash, url_for
from werkzeug.security import generate_password_hash

from app.auth import auth
from app.auth.models import Users, Profiles
from app.main_menu import menu


@auth.route("/login", methods=["POST", "GET"])
def login():
    title = "Login"
    return render_template("login.html",
                           title=title, menu=menu)


@auth.route("/register", methods=("POST", "GET"))
def register():
    if request.method == "POST":

        # add wtforms and CSRF
        if len(request.form['name']) > 4 and len(request.form['email']) > 4 \
                and len(request.form['psw']) > 4 and request.form['psw'] == request.form['psw2']:
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
            return redirect(url_for('main.index'))
        else:
            flash("Неверно заполнены поля", "error")

    title = "Registration"
    return render_template("register.html",
                           title=title,
                           menu=menu)
