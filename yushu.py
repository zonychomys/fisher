# -*- coding: utf-8 -*-

from httper import HTTP


class YuShu(object):
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, start=0, count=15):
        url = cls.keyword_url.format(keyword, start, count)
        result = HTTP.get(url)
        return result
