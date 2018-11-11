# -*- coding: utf-8 -*-

from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length, DataRequired, Email, ValidationError
from app.models.user import User


class RegisterForm(Form):
    email = StringField(
        validators=[DataRequired(),
                    Length(8, 64),
                    Email(message='错误的邮箱格式')])
    password = PasswordField(
        validators=[DataRequired(
            message='密码不能为空'), Length(6, 32)])
    nickname = StringField(
        validators=[DataRequired(),
                    Length(2, 10, message='昵称长度为2-10个字符')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('用户名已注册')


class LoginForm(Form):
    email = StringField(
        validators=[DataRequired(),
                    Length(8, 64),
                    Email(message='错误的邮箱格式')])
    password = PasswordField(
        validators=[DataRequired(
            message='密码不能为空'), Length(6, 32)])
