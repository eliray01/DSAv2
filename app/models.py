from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from hashlib import md5
from flask import session


user_project = db.Table("user_project",
                        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                        db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
                        )

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    following = db.relationship('Project', secondary = user_project, backref='followers')

    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    preferences = db.Column(db.String(500))
    usertype = db.Column(db.String(120))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=mp&s={}'.format(
            digest, size)


    def __repr__(self):
        return '<User {}>'.format(self.username)


class Project(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    body = db.Column(db.String(140))
    describe = db.Column(db.String(140))
    type = db.Column(db.String(140))
    view = db.Column(db.String(140))
    current_number_of_students = db.Column(db.Integer, default = 0)
    max_students = db.Column(db.Integer)
    name = db.Column(db.String(140))
    def __repr__(self):
        return '<Project {}>'.format(self.body)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

