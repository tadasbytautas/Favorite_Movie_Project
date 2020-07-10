from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_login import current_user




class PostForm(FlaskForm):
    title = StringField(
        'Movie Title: ',
        validators=[
            DataRequired(),
            Length(min=1, max=100)
        ]
    )

    content = StringField(
        'Movie Storyline: ',
        validators=[
            DataRequired(),
            Length(min=1, max=1000)
        ]
    )

    submit = SubmitField('Make a Post')

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
         validators=[
             DataRequired(),
             Length(min=2, max=30)
         ])
    last_name = StringField('Last Name',
        validators=[
            DataRequired(),
            Length(min=3, max=30)
        ])
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password',
        validators = [
            DataRequired(),
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    last_name = StringField('Last Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ])
    submit = SubmitField('Update')

class UpdatePostDetails(FlaskForm):
    title = StringField(
        'Movie Title: ',
        validators=[
            DataRequired(),
            Length(min=1, max=100)
        ]
    )

    content = StringField(
        'Movie Storyline: ',
        validators=[
            DataRequired(),
            Length(min=1, max=1000)
        ]
    )

    submit = SubmitField('Update')