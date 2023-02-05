from flask import render_template
from flask_login import login_required

from app.about import about
from app.auth.models import Users
from app.main_menu import menu


@about.route("/about", methods=["POST", "GET"])
@login_required
def about():
    info = Users.select()
    title = "About"
    return render_template("about.html",
                           title=title,
                           menu=menu,
                           list=info)

