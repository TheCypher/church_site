from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from .decorators import *
from .forms import *

mod = Blueprint('admin', __name__, url_prefix='/admin')

@mod.before_request
def before_request():
	g.user = None
	if 'user_id' in session:
		g.user = 1

@mod.route('/', methods=['GET', 'POST'])
@mod.route('/home', methods=['GET', 'POST'])
@login_required
def index():
	page = {
		'title':'Home'
	}
	return render_template('admin/index.html', page=page)

@mod.route('/logout', methods=['GET'])
@login_required
def logout():
	session['user_id'] = ''
	return redirect(url_for('front.signin'))

@mod.route('/website', methods=['GET', 'POST'])
@login_required
def website():
	page = {
		'title':'Website'
	}
	return render_template('admin/website.html', page=page)

@mod.route('/edit-page', methods=['GET', 'POST'])
def edit_page():
	pageName = 'Homepage'
	page = {
		'title':'Edit - %s' % (pageName)
	}

	form = [
		{'name':'big_header', 'type':'text', 'class':'form-control', 'label':'header'},
		{'name':'top_text', 'type':'text', 'class':'form-control', 'label':'top'},
		{'name':'bottom_text', 'type':'text', 'class':'form-control', 'label':'bottom'},
		{'name':'bg_header', 'type':'text', 'class':'form-control', 'label':'Background Image'}
	]

	htmlForms = generateForms(form)
	print(htmlForms[0])

	return render_template('admin/edit-page.html', page=page, forms=htmlForms[0])
