# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.models.base import Base
from flask import current_app


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    isbn = Column(String(13))
    launched = Column(Boolean, default=False)

    def recent(self):
        recent_gift = Gift.query.filter_by(launched=False).group_by(
            Gift.isbn).order_by(Gift.create_time).limit(
                current_app.config['RECENT_BOOK_COUNT']).all()
        return recent_gift
