from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    userID = StringField(
        'User: ',
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