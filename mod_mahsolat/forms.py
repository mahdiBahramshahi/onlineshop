from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import FileField , SelectField , StringField , BooleanField , TextField , SubmitField
from mod_mahsolat.models import MahsolGroups

class MahsolatForms(FlaskForm):
    mahsol_title = TextField(validators=[DataRequired()])
    description = TextField(validators=[DataRequired()])
    groups = MahsolGroups.query.order_by(MahsolGroups.id.desc()).all()
    mahsol_category = SelectField(u'mahsol category', choices=[('-', '-'),('', '')])
    mahsol_price = TextField(validators=[DataRequired()])
    mahsol_description = TextField(validators=[DataRequired()])
    mahsol_image = TextField(validators=[DataRequired()])

class MahsolgroupForms(FlaskForm):
    group_name = TextField(validators=[DataRequired()])
    group_image = TextField(validators=[DataRequired()])

class SearchForm(FlaskForm):
    search_query = TextField(validators=[DataRequired()])
