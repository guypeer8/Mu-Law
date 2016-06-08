from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import Required, Length, Email

class VisitorForm(Form):
    name = StringField('', validators=[Required(), Length(2, 16)])
    email = StringField('', validators=[Required(), Length(9, 36), Email()])
    text = TextAreaField('', validators=[Required(), Length(2, 200)])
