from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from passlib.hash import pbkdf2_sha256

from .decorators import *
from app.admin.models import Users

mod = Blueprint('front', __name__, url_prefix='')

@mod.before_request
def before_request():
	g.user = None
	if 'user_id' in session:
		g.user = Users.query.get(session['user_id'])


@mod.route('/', methods=['GET'])
def index():
	page = {
		'page':'Home',
		'style': {}
	}
	return render_template("front/index.html", page=page)

@mod.route('/about', methods=['GET'])
def about():
	page = {
		'page':'About',
		'style': {}
	}
	return render_template("front/about.html", page=page)

@mod.route('/contact', methods=['GET', 'POST'])
def contact():
	page = {
		'page':'Contact',
		'style': {'navbar':'navbar-fixed-top'}
	}
	return render_template("front/contact.html", page=page)

@mod.route('/signin', methods=['GET', 'POST'])
@already_login
def signin():
	page = {
		'page':'Signin',
		'style': {}
	}
	if request.method != 'POST':
		return render_template('front/signin.html', page=page)

	user_data = {
		'email': request.form['email'],
		'password': request.form['password']
	}

	for key, value in user_data.items():
		if value == '':
			page['error'] = 'All fields must be filled'
			return render_template('front/signin.html', page=page)

	userModels = Users()
	user = userModels.checkEmail(user_data['email'])
	
	if not user or not verifyPassword(user_data['password'], user.password):
		page['error'] = 'Wrong email or password'
		return render_template('front/signin.html', page=page)

	session['user_id'] = user.id
	return redirect(url_for('admin.index'))

@mod.route('/signup', methods=['GET', 'POST'])
@already_login
def signup():
	page = {
		'page':'Signup',
		'style': {}
	}

	if request.method != 'POST':
		return render_template('front/signup.html', page=page)

	user_data = {
		'firstname':request.form['firstname'],
		'lastname': request.form['lastname'],
		'email': request.form['email'],
		'password': request.form['password']
	}

	for key, value in user_data.items():
		if value == '':
			page['error'] = 'All fields must be filled'
			return render_template('front/signup.html', page=page)

	userModels = Users()

	if  userModels.checkEmail(user_data['email']):
		page['error'] = 'This user already exists'
		return render_template('front/signup.html', page=page)
	
	user_data['password'] = hashPassword(user_data['password']) 
	user = Users(**user_data)
	db.session.add(user)
	db.session.commit()
	session['user_id'] = user.id
	return redirect(url_for('.index'))

def hashPassword(password):
	return pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)

def verifyPassword(formPass, dbPass):
	return pbkdf2_sha256.verify(formPass, dbPass)

