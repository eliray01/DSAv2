from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    #username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    usertype = SelectField('User Type', choices=[("Student","Student"),("Teacher","Teacher")],validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    preferences = TextAreaField('Academic interests', validators=[Length(min=0, max=500)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

class AddProjectForm(FlaskForm):
    body = StringField('Name of the project', validators=[DataRequired()])
    describe = TextAreaField('Link to the project file', validators=[Length(min=0, max=140)])
    type = SelectField('Project type', choices=[("Research","Research"),("Software","Software")],validators=[DataRequired()])
    view = SelectField('View of the project', choices=[("Individual","Individual"),("Team","Team")],validators=[DataRequired()])
    max_students = SelectField(coerce=int, label = 'Maximum number of students', choices=[(1,1),(2,2),(3,3),(4,4)],validators=[DataRequired()])
    name = StringField('Your name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ContactForm(FlaskForm):
    submit = SubmitField('Do this')
    submit2 = SubmitField('Do that')


