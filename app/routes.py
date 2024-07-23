# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, send_file, send_from_directory, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.forms import lit_form, seal_form, thread_form_gn, thread_form_rkv
from app.models import db, User, parts, lit_results, seal_results, thread_results
import sqlite3
from datetime import datetime
from datetime import date
from  time import  strftime
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неверное имя пользователя или пароль')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login.html', title='Вход в систему', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, fio=form.fio.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Вы успешно зарегистрировались в системе. Обязательно запомните свой логин и пароль.')
        return redirect(url_for('login'))
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/lit_check', methods=['GET', 'POST'])
@login_required
def lit():
    i = request.args.get('i')
    form = lit_form(i)
    match i:
        case '1':
            lit = '/static/CO_sRKN.png'
        case '2':
            lit = '/static/RKV_sl.png'
        case '3':
            lit = '/static/MT_s.png'
        case '4':
            lit = '/static/MSM_s.png'
        case '5':
            lit = '/static/GN_s.png'
        case '6':
            lit = '/static/GZ_s.png'
        case '7':
            lit = '/static/OK_s.png'

    if form.validate_on_submit():
        part = form.part.data
        pereliv = form.pereliv.data
        flag = form.flag.data
        svish = form.svish.data
        neproliv = form.neproliv.data
        nedoliv = form.nedoliv.data
        parameter_name = ['переливы', 'флажок','свищи','непроливы','недоливы']
        parameters = [pereliv, flag, svish, neproliv, nedoliv]
        failed_parameters=[]
        for i in range(5):
            if parameters[i] == 1:
                pass
            elif parameters[i] == 0:
                failed_parameters.append(f'{parameter_name[i]}')
        defects = f'{", ".join(failed_parameters)}'
        try:        
            current_time = datetime.now().strftime("%H:%M:%S")
            new_ln = lit_results(surname=current_user.fio, date=date.today(), time=current_time,part=part,defects=defects)
            db.session.add(new_ln)
            db.session.commit()
            flash('Данные успешно сохранены')
        except:
            flash('Данные не были сохранены')
        finally:
            pass
        return redirect(url_for('index'))
    return render_template('lit.html', title='Цинковое литье', form=form, lit=lit)

@app.route('/seal_check', methods=['GET', 'POST'])
@login_required
def seal():
    i = request.args.get('i')
    form = seal_form(i)
    match i:
        case '1':
            seal_pic = 'UO_s.png'
        case '2':
            seal_pic = 'UZ_s.png'
    if form.validate_on_submit():
        part = form.part.data
        nezapolnenie = form.nezapolnenie.data
        obloy = form.obloy.data
        razryv = form.razryv.data
        parameter_name = ['незаполнение', 'облой','разрыв']
        parameters = [nezapolnenie,obloy,razryv]
        failed_parameters=[]
        for i in range(3):
            if parameters[i] == 1:
                pass
            elif parameters[i] == 0:
                failed_parameters.append(f'{parameter_name[i]}')
        defects = f'{", ".join(failed_parameters)}'
        try:        
            current_time = datetime.now().strftime("%H:%M:%S")
            new_ln = seal_results(surname=current_user.fio, date=date.today(), time=current_time,part=part,defects=defects)
            db.session.add(new_ln)
            db.session.commit()
            flash('Данные успешно сохранены')
        except:
            flash('Данные не были сохранены')
        finally:
            pass
        return redirect(url_for('index'))
    return render_template('seal.html', title='Цинковое литье', form=form, seal_pic=seal_pic)

@app.route('/thread_check', methods=['GET', 'POST'])
@login_required
def thread():
    i = request.args.get('i')
    match i:
        case '1':
            page = 'thread_rkv.html'
            form = thread_form_rkv()
            if form.validate_on_submit():
                part = form.part.data
                prohod = form.prohod.data
                neprohod = form.neprohod.data
                parameter_name = ['проходной', 'непроходной']
                parameters = [prohod, neprohod]
                failed_parameters=[]
                for i in range(2):
                    if parameters[i] == 1:
                        pass
                    elif parameters[i] == 0:
                        failed_parameters.append(f'{parameter_name[i]}')
                defects = f'{", ".join(failed_parameters)}'
                try:        
                    current_time = datetime.now().strftime("%H:%M:%S")
                    new_ln = thread_results(surname=current_user.fio, date=date.today(), time=current_time,part=part,defects=defects)
                    db.session.add(new_ln)
                    db.session.commit()
                    flash('Данные успешно сохранены')
                except:
                    flash('Данные не были сохранены')
                finally:
                    pass
                return redirect(url_for('index'))
        case '2':
            page = 'thread_gn.html'
            form = thread_form_gn()
            if form.validate_on_submit():
                part = form.part.data
                sobiraemost = form.sobiraemost.data
                parameter_name = ['собираемость']
                parameters = [sobiraemost]
                failed_parameters=[]
                for i in range(1):
                    if parameters[i] == 1:
                        pass
                    elif parameters[i] == 0:
                        failed_parameters.append(f'{parameter_name[i]}')
                defects = f'{", ".join(failed_parameters)}'
                try:        
                    current_time = datetime.now().strftime("%H:%M:%S")
                    new_ln = thread_results(surname=current_user.fio, date=date.today(), time=current_time,part=part,defects=defects)
                    db.session.add(new_ln)
                    db.session.commit()
                    flash('Данные успешно сохранены')
                except:
                    flash('Данные не были сохранены')
                finally:
                    pass
                return redirect(url_for('index'))
    
    return render_template(page, title='Нарезание резьбы', form=form)