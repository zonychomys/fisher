# -*- coding: utf-8 -*-

from flask import Flask
from app.web import web
from app.models.book import db

# 该语句决定了应用程序app的根目录是app而不是fisher
app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config.from_object('app.config')
app.register_blueprint(web)
db.init_app(app)
db.create_all(app=app)
