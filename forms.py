from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class PostForm(FlaskForm):
    userID = StringField(
        'UserID: ',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    title = StringField(
        'Movie Title: ',
        validators=[
            DataRequired(),
            Length(min=4, max=100)
        ]
    )

    content = StringField(
        'Movie Description: ',
        validators=[
            DataRequired(),
            Length(min=4, max=300)
        ]
    )

    submit = SubmitField('Make a Post')

class RegistrationForm(FlaskForm):
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