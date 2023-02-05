from flask import render_template

from app.auth import auth
from app.main_menu import menu


@auth.route("/login", methods=["POST", "GET"])
def login():
    title = "Login"
    return render_template("login.html",
                           title=title, menu=menu)


@auth.route("/register", methods=["POST", "GET"])
def register():
    title = "Registration"
    return render_template("register.html",
                           title=title, menu=menu)
