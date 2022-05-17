from flask_wtf import FlaskForm, Form

from wtforms import StringField, SubmitField

from wtforms.validators import InputRequired, Email


class SimpleWebForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), Email()])
    submit = SubmitField("Submit")
