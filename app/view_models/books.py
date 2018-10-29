# -*- coding: utf-8 -*-


class BookViewModel(object):
    @classmethod
    def package_single(cls, data, keyword):
        returned = {'books': [], 'total': 0, 'keyword': keyword}
        if data:
            returned['total'] = 1
            returned['books'] = [cls._cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {'books': [], 'total': 0, 'keyword': keyword}
        if data:
            returned['total'] = data['total']
            returned['books'] = [
                cls._cut_book_data(book) for book in data['books']
            ]
        return returned

    @classmethod
    def _cut_book_data(cls, data):
        book = {
            'total': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book
