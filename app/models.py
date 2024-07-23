# -*- coding: utf-8 -*-
from app import db, login
from datetime import datetime
from sqlalchemy import Float
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

### изделия
class parts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	part = db.Column(db.String(64), index=True)
	part_type = db.Column(db.String(64), index=True)
	part_group = db.Column(db.String(64), index=True)

### литье
class lit_results(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	surname = db.Column(db.String(64), index=True)
	date = db.Column(db.String(64), index=True)
	time = db.Column(db.String(64), index=True)
	part = db.Column(db.String(64), index=True)
	defects = db.Column(db.String(64), index=True)
	reason = db.Column(db.String(64), index=True)

### резина
class seal_results(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	surname = db.Column(db.String(64), index=True)
	date = db.Column(db.String(64), index=True)
	time = db.Column(db.String(64), index=True)
	part = db.Column(db.String(64), index=True)
	defects = db.Column(db.String(64), index=True)
	reason = db.Column(db.String(64), index=True)

### резьба
class thread_results(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	surname = db.Column(db.String(64), index=True)
	date = db.Column(db.String(64), index=True)
	time = db.Column(db.String(64), index=True)
	part = db.Column(db.String(64), index=True)
	defects = db.Column(db.String(64), index=True)

### Таблица пользователей
class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	fio = db.Column(db.String(64), index=True)
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		return '<User {}>'.format(self.username)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)
		
	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))