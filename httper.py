# -*- coding: utf-8 -*-

import requests


class HTTP(object):
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code == 200:
            return r.json() if return_json else r.text
        else:
            return {} if return_json else ''
