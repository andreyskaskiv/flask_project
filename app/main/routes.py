from flask import render_template, current_app, flash

from app.auth.models import Users, Profiles
from app.main import main
from app.main_menu import menu
from database.create_database import create_db


@main.route('/')
def index():
    db = current_app.config['db']
    create_db(db, Users, Profiles)
    title = "Home"
    return render_template("index.html",
                           title=title,
                           menu=menu)  # , list=info)
