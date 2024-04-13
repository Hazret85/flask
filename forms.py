from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField


class ProductForm(FlaskForm):
    name = StringField('Название')
    description = StringField('Описание')
    price = StringField('Цена')
    submit = SubmitField('Добавить')


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Register')
