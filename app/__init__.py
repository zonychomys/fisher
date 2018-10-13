# -*- coding: utf-8 -*-

from flask import Flask
from app.web import web

app = Flask(__name__)
app.register_blueprint(web)