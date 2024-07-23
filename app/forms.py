# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField, SelectField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, EqualTo
from app.models import User
import sqlite3

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], render_kw={'style': 'font-size: 30px; text-align: center'})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={'style': 'font-size: 30px; text-align: center'})
    remember_me = BooleanField('Запомнить меня', render_kw={'style': 'transform:scale(1.5)'})
    submit = SubmitField('Войти', render_kw={'style': 'font-size: 40px; text-align: center'})

class RegistrationForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], render_kw={'style': 'font-size: 40px; text-align: center'})
    fio = StringField('Ваше ФИО', validators=[DataRequired()], render_kw={'style': 'font-size: 40px; text-align: center'})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={'style': 'font-size: 40px; text-align: center'})
    password2 = PasswordField(
        'Повторите пароль', validators=[DataRequired(), EqualTo('password')], render_kw={'style': 'font-size: 40px; text-align: center'})
    submit = SubmitField('Регистрация', render_kw={'style': 'font-size: 40px; text-align: center'})

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Данное имя уже используется.')

class lit_form(FlaskForm):
    part = SelectField('Деталь', choices=[], render_kw={'class': 'select-field', 'style': 'font-size: 30px; text-align: left; width: 160'})
    pereliv = BooleanField('Переливы:', render_kw={'style': 'transform:scale(2); margin-top: 0px; margin-bottom: 0px'})
    flag = BooleanField('Флажок:', render_kw={'style': 'transform:scale(2); margin-top: 0px; margin-bottom: 0px'})
    svish = BooleanField('Свищи:', render_kw={'style': 'transform:scale(2); margin-top: 0px; margin-bottom: 0px'})
    neproliv = BooleanField('Непроливы:', render_kw={'style': 'transform:scale(2); margin-top: 0px; margin-bottom: 0px'})
    nedoliv = BooleanField('Недоливы:', render_kw={'style': 'transform:scale(2); margin-top: 0px; margin-bottom: 0px'})
    submit = SubmitField('Подтвердить', render_kw={'style': 'font-size: 35px; text-align: center'})

    def __init__(self, i, *args, **kwargs):
        super(lit_form, self).__init__(*args, **kwargs)
        match i:
            case '1':
                self.part.choices = self.get_part_choices(part_type='RKN')
            case '2':
                self.part.choices = self.get_part_choices(part_type='RKV')
            case '3':
                self.part.choices = self.get_part_choices(part_type='MT')
            case '4':
                self.part.choices = self.get_part_choices(part_type='MSM')
            case '5':
                self.part.choices = self.get_part_choices(part_type='GN')
            case '6':
                self.part.choices = self.get_part_choices(part_type='GZ')
            case '7':
                self.part.choices = self.get_part_choices(part_type='OK')
   
    def get_part_choices(self, part_type):
        try:    
            conn = sqlite3.connect('fit.db')
            cursor = conn.cursor()
            cursor.execute("SELECT part FROM parts WHERE part_type = ?", (part_type,))
            sz = cursor.fetchall()
            conn.close()
            return [(row[0], row[0]) for row in sz]
        except Exception as e:
            print(e)
            return []


class seal_form(FlaskForm):
    part = SelectField('Деталь', choices=[], render_kw={'class': 'select-field', 'style': 'font-size: 30px; text-align: left; width: 160'})
    nezapolnenie = BooleanField('Незаполнения', render_kw={'style': 'transform:scale(2); margin-top: 0px; margin-bottom: 0px'})
    obloy = BooleanField('Облой', render_kw={'style': 'transform:scale(2); margin-top: 0px; margin-bottom: 0px'})
    razryv = BooleanField('Разрывы', render_kw={'style': 'transform:scale(2); margin-top: 0px; margin-bottom: 0px'})
    submit = SubmitField('Подтвердить', render_kw={'style': 'font-size: 35px; text-align: center'})

    def __init__(self, i, *args, **kwargs):
        super(seal_form, self).__init__(*args, **kwargs)
        match i:
            case '1':
                self.part.choices = self.get_part_choices(part_type='UO')
            case '2':
                self.part.choices = self.get_part_choices(part_type='UZ')
   
    def get_part_choices(self, part_type):
        try:    
            conn = sqlite3.connect('fit.db')
            cursor = conn.cursor()
            cursor.execute("SELECT part FROM parts WHERE part_type = ?", (part_type,))
            sz = cursor.fetchall()
            conn.close()
            return [(row[0], row[0]) for row in sz]
        except Exception as e:
            print(e)
            return []
        
class thread_form_rkv(FlaskForm):
    part = SelectField('Part', choices=[], render_kw={'class': 'select-field', 'style': 'font-size: 30px; text-align: left; width: 160'})
    prohod = BooleanField('Проходной калибр:', render_kw={'style': 'transform:scale(2); margin-top: 0px; margin-bottom: 0px'})
    neprohod = BooleanField('Непроходной калибр:', render_kw={'style': 'transform:scale(2); margin-top: 0px; margin-bottom: 0px'})
    submit = SubmitField('Подтвердить', render_kw={'style': 'font-size: 35px; text-align: center'})

    def __init__(self, *args, **kwargs):
        super(thread_form_rkv, self).__init__(*args, **kwargs)
        self.part.choices = self.get_part_choices(part_type='RKV')
   
    def get_part_choices(self, part_type):
        try:    
            conn = sqlite3.connect('fit.db')
            cursor = conn.cursor()
            cursor.execute("SELECT part FROM parts WHERE part_type = ?", (part_type,))
            sz = cursor.fetchall()
            conn.close()
            return [(row[0], row[0]) for row in sz]
        except Exception as e:
            print(e)
            return []

class thread_form_gn(FlaskForm):
    part = SelectField('Деталь', choices=[], render_kw={'class': 'select-field', 'style': 'font-size: 30px; text-align: left; width: 160'})
    sobiraemost = BooleanField('Собираемость с образцами корпусов', render_kw={'style': 'transform:scale(2); margin-top: 0px; margin-bottom: 0px'})
    submit = SubmitField('Подтвердить', render_kw={'style': 'font-size: 35px; text-align: center'})

    def __init__(self, *args, **kwargs):
        super(thread_form_gn, self).__init__(*args, **kwargs)
        self.part.choices = self.get_part_choices(part_type='GN')
   
    def get_part_choices(self, part_type):
        try:    
            conn = sqlite3.connect('fit.db')
            cursor = conn.cursor()
            cursor.execute("SELECT part FROM parts WHERE part_type = ?", (part_type,))
            sz = cursor.fetchall()
            conn.close()
            return [(row[0], row[0]) for row in sz]
        except Exception as e:
            print(e)
            return []