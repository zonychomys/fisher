# -*- coding: utf-8 -*-

import json

from flask import jsonify, request, render_template, flash
from app.forms.book import SearchForm
from app.lib.helper import is_isbn_or_key
from app.spider.yushu import YuShu
from app.view_models.books import BookCollection, BookViewModel
from . import web


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu = YuShu()
        if isbn_or_key == 'isbn':
            yushu.search_by_isbn(q)
        else:
            yushu.search_by_keyword(q, page)
        books.fill(yushu, q)
        # return json.dumps(books, default=lambda x: x.__dict__)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
        # return jsonify({'msg': form.errors})
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu = YuShu()
    yushu.search_by_isbn(isbn)
    book = BookViewModel(yushu.first)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])
