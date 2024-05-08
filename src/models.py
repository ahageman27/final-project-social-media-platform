from src import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship

class User(db.Model, UserMixin):
	__tablename__ = 'users'

	name = db.Column(db.String(64), primary_key=True)
	# TODO: someone should make this more secure. i don't feel like it
	password_hash = db.Column(db.String(64), nullable=False)

	def get_id(self):
		return self.name
