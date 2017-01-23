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
