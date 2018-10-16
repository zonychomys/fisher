# -*- coding: utf-8 -*-

import wtforms
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(wtforms.Form):
    q = wtforms.StringField(validators=[Length(min=1, max=10), DataRequired()])
    page = wtforms.IntegerField(
        validators=[NumberRange(min=1, max=99)], default=1)
