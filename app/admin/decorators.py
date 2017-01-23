from functools import wraps
from flask import g, flash, url_for, redirect, request

def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if g.user is None:
			flash(u'Please sign in')
			return redirect(url_for('front.signin', next=request.path))
		return f(*args, **kwargs)
	return decorated_function

