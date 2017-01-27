from time import strftime

from app import db

dateNow = strftime("%a, %d %b %Y")

class Users(db.Model):
	__tablename__ = 'users'
	id = db.Column('id', db.Integer, primary_key=True)
	firstname = db.Column('firstname', db.String(80))
	lastname = db.Column('lastname', db.String(80))
	email = db.Column('email', db.String(80))
	password = db.Column('password', db.String(255))
	signed_up_on = db.Column('signed_up_on', db.String(255))

	def __inti__(self, **user):
		if user:
			self.firstname = user['firstname'],
			self.lastname = user['lastname'],
			self.email = user['email'],
			self.password = user['password'],
			self.signed_up_on = dateNow

	def getUserLogin(self, **user):
		print(user)
		return self.query.filter_by(email=user['email'], password=user['password']).first()
	
	def checkEmail(self, email):
		return self.query.filter_by(email=email).first()


class Homepage_section_one(db.Model):
	__tablename__ = 'homepage_section_one'
	id = db.Column('id', db.Integer, primary_key=True)
	page_name = db.Column('page_name', db.String(80))
	headerImg = db.Column('headerImg', db.String(255))
	headerText = db.Column('headerText', db.String(255))
	topText = db.Column('topText', db.String(255))
	middleText = db.Column('middleText', db.String(255))
	bottomText = db.Column('bottomText', db.String(255))

class Homepage_section_two(db.Model):
	__tablename__ = 'homepage_section_two'
	id = db.Column('id', db.Integer, primary_key=True)
	bigText = db.Column('bigText', db.String(255))
	smallText = db.Column('smallText', db.String(255))
	Img = db.Column('Img', db.String(255))

class Homepage_section_three(db.Model):
	__tablename__ = 'homepage_section_three'
	id = db.Column('id', db.Integer, primary_key=True)
	smallText = db.Column('smallText', db.String(255))
	bigText = db.Column('bigText', db.String(255))
	smallText2 = db.Column('smallText2', db.String(255))
	projectImgs = db.Column('projectImgs', db.String(255))

class Homepage_section_four(db.Model):
	__tablename__ = 'homepage_section_four'
	id = db.Column('id', db.Integer, primary_key=True)
	bigText = db.Column('bigText', db.String(255))
	smallText = db.Column('smallText', db.String(255))
	Img = db.Column('Img', db.String(255))

