from wtforms import Form, StringField
from wtforms.validators import DataRequired


class NoteForm(Form):

    title = StringField(validators=[DataRequired()])
    content = StringField(validators=[DataRequired()])
