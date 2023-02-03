from flask import render_template

from app.main import main


menu = [{'url': 'main.index', 'title': 'HOME'},
        {'url': 'about.about', 'title': 'ABOUT'},]
        # {'url': '.listpubs', 'title': 'Список статей'},
        # {'url': '.logout', 'title': 'Выйти'}]

@main.route('/')
def index():
    title = "Home"
    return render_template("index.html",
                           title=title,
                           menu=menu)#, list=info)

