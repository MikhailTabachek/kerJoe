from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class JokePostForm(FlaskForm):
    title = StringField('Title(2-3 words)', validators=[DataRequired()])
    text = TextAreaField('Your Joke( a funny one...)', validators=[DataRequired()])
    submit = SubmitField('Post')