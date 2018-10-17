# -*- coding: utf-8 -*-

from flask import Flask
from app.web import web
from app.models.book import db

app = Flask(__name__)
app.config.from_object('app.config')
app.register_blueprint(web)
db.init_app(app)
db.create_all(app=app)
