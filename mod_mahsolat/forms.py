from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import FileField , SelectField , StringField , BooleanField , TextField , SubmitField


class MahsolatForms(FlaskForm):
    mahsol_title = TextField(validators=[DataRequired()])
    description = TextField(validators=[DataRequired()])
    mahsol_category = SelectField(u'mahsol category', choices=[('-', '-'),('یک طول', 'یک طول'), ('دو طول', 'دو طول'), ('چهار طرف', 'چهار طرف') , ('یک عرض', 'یک عرض')])
    mahsol_price = TextField(validators=[DataRequired()])
    mahsol_description = TextField(validators=[DataRequired()])
    mahsol_image = TextField(validators=[DataRequired()])

