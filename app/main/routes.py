from flask import render_template

from app.main import main


@main.route('/')
def index():
    title = "Главная"
    return render_template("index.html",
                           title=title)#,
                           #menu=menu, list=info)

