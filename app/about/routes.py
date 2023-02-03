from flask import render_template

from app.about import about


@about.route("/about", methods=["POST", "GET"])
def about():
    title = "About"
    return render_template("about.html",
                           title=title)  # ,menu=menu)

