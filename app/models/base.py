# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, SmallInteger
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)
