# -*- coding: utf-8 -*-
"""
对api返回的结果进行整理，无论是单条数据还是多条数据，统一成相同的数据结构
"""

from flask import current_app
from app.lib.httper import HTTP


class YuShu(object):
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_conllection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, self.calculate_start(page),
                                      current_app.config['PER_PAGE'])
        result = HTTP.get(url)
        self.__fill_conllection(result)

    def calculate_start(self, page):
        return (page - 1) * current_app.config['PER_PAGE']
