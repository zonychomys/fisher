# -*- coding: utf-8 -*-

from flask import jsonify
from helper import is_isbn_or_key
from yushu import YuShu
from . import web


@web.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShu.search_by_isbn(q)
    else:
        result = YuShu.search_by_keyword(q)
    return jsonify(result)
