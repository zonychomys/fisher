# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, desc, func
from sqlalchemy.orm import relationship
from app.models.base import db, Base
from app.models.wish import Wish
from flask import current_app
from app.spider.yushu import YuShu


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    isbn = Column(String(13))
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(
            uid=uid, launched=False).order_by(desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(
            Wish.launched == False, Wish.isbn.in_(isbn_list),
            Wish.status == 1).group_by(Wish.isbn).all()
        count_list  = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushu = YuShu()
        yushu.search_by_isbn(self.isbn)
        return yushu.first

    @classmethod
    def recent(self):
        recent_gift = Gift.query.filter_by(launched=False).group_by(
            Gift.isbn).order_by(desc(Gift.create_time)).limit(
                current_app.config['RECENT_BOOK_COUNT']).all()
        return recent_gift
