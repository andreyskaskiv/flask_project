from flask import Blueprint

about = Blueprint('about', __name__)

from app.about import routes