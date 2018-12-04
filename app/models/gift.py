# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, desc
from sqlalchemy.orm import relationship
from app.models.base import Base
from flask import current_app
from app.spider.yushu import YuShu


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    isbn = Column(String(13))
    launched = Column(Boolean, default=False)

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
