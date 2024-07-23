# -*- coding: utf-8 -*-
from app import app, db
from app.models import User, parts, lit_results, seal_results, thread_results
import sqlite3

@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User,
			'parts': parts,
			'lit_results': lit_results,
			'seal_results': seal_results,
			'thread_results': thread_results}
