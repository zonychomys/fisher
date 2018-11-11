# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, SmallInteger
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    # 告诉sqlalchemy无需为此model创建数据库表
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)
