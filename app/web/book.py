# -*- coding: utf-8 -*-
from flask import request, render_template, flash
from flask_login import current_user
from app.models.gift import Gift
from app.models.wish import Wish
from app.forms.book import SearchForm
from app.lib.helper import is_isbn_or_key
from app.spider.yushu import YuShu
from app.view_models.books import BookCollection, BookViewModel
from app.view_models.trade import TradeInfo
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
    has_in_gifts = False
    has_in_wishes = False
    # 取书籍详细数据
    yushu = YuShu()
    yushu.search_by_isbn(isbn)
    book = BookViewModel(yushu.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(
                uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = False
        if Wish.query.filter_by(
                uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_wishes = False

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()
    trade_gifts_model = TradeInfo(trade_gifts)
    trade_wishes_model = TradeInfo(trade_wishes)

    return render_template(
        'book_detail.html',
        book=book,
        wishes=trade_wishes_model,
        gifts=trade_gifts_model,
        has_in_gifts=has_in_gifts,
        has_in_wishes=has_in_wishes)
