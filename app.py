#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import Flask, jsonify
from helper import is_isbn_or_key
from yushu import YuShu

app = Flask(__name__)


@app.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShu.search_by_isbn(q)
    else:
        result = YuShu.search_by_keyword(q)
    return jsonify(result)


app.run(host='0.0.0.0', port=5000)
