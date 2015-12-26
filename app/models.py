# from wtforms_components import ModelForm

__author__ = 'Azad'
from app import db
from wtforms.fields import TextField, IntegerField
from wtforms.validators import Email, Optional
from datetime import datetime

# class User(db.Model):
#     user_id = db.Column(db.Integer,primary_key=True)
#     user_email = db.Column(db.String(50),unique=True)
#     user_fullName = db.Column(db.String(50))
#

#create Question model
# class Question (db.Model):
#     questionID = db.Column(db.Integer,primary_key=True)
#     description = db.Column(db.String(300),unique=True)
#     categoryID = db.Column(db.Integer, db.ForeignKey('category.ID'))
#     userID = db.Column(db.Integer, db.ForeignKey('registertable.ID'))
#     option1 = db.Column(db.String(100))
#     option2 = db.Column(db.String(100))
#     option3 = db.Column(db.String(100))
#     option4 = db.Column(db.String(100))
#     correctAnswer = db.Column(db.Integer)
#     hint = db.Column(db.String(300))
#     solvedUser = db.Column(db.Integer)
#     failedUser = db.Column(db.Integer)
#     imgURL = db.Column(db.String(300))
#     dateUploaded = db.Column(db.DateTime)
#
# class Category(db.Model):
#     ID = db.Column(db.Integer,primary_key=True)
#     category = db.Column(db.String(300))
#     subject = db.Column(db.String(300))
#     questions = db.relationship('Question',backref='category',lazy='dynamic')
#
# class School(db.Model):
#     schoolID = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(300))
#     registertable = db.relationship('Registertable', backref='school', lazy='dynamic')
# class SolveProblems(db.Model):
#     ID = db.Column(db.Integer,primary_key=True)
#     userID = db.Column(db.Integer)
#     questionID = db.Column(db.Integer,unique=False)
#
#
# class Registertable (db.Model):
#     ID = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(300))
#
#     email = db.Column(db.String(100), unique=True)
#     userID = db.Column(db.String(300),unique=True)
#     password = db.Column(db.String(100))
#     gender = db.Column(db.Boolean, unique=False)
#     imgURL = db.Column(db.String(100), unique=True)
#     solved = db.Column(db.Integer)
#     unsolved = db.Column(db.Integer)
#     # Flask-Login integration
#     def is_authenticated(self):
#         return True
#
#     def is_active(self):
#         return True
#
#     def is_anonymous(self):
#         return False
#
#     def get_id(self):
#         return self.ID
#
#     # Required for administrative interface
#     def __unicode__(self):
#         return self.name
#     def check_password(self, password):
#
# 	    return password == self.password

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(64), index=True)
    lastName = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(120), index=True)
    #addresses = db.relationship('Address',  back_populates="user")

    def __repr__(self):
        return '<User %r>' % (self.nickname)

# class UserForm(ModelForm):
#     class Meta:
#         model = User
#
#     email = TextField(validators=[Optional()])


# class Address(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#
#     user = db.relationship("User", back_populates="addresses")
#
#     def __repr__(self):
#         return '<Post %r>' % (self.body)