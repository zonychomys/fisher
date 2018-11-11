# -*- coding: utf-8 -*-

from sqlalchemy import Column, SmallInteger
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    # 告诉sqlalchemy无需为此model创建数据库表
    __abstract__ = True
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for k, v in attrs_dict.items():
            if hasattr(self, k) and k != 'id':
                setattr(self, k, v)
