from functools import wraps

from flask import g, flash, redirect, url_for, request

def already_login(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if g.user:
			return redirect(url_for('admin.index'))
		return f(*args, **kwargs)
	return decorated_function
