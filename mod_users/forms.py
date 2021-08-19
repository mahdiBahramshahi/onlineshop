from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import PasswordField , StringField , TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])


class RegisterForm(FlaskForm):
    username= StringField(validators=[DataRequired()])
    email= EmailField(validators=[DataRequired()])
    password= PasswordField(validators=[DataRequired()])
    confirm_password = PasswordField(validators=[DataRequired()])
    phone_number = StringField(validators=[DataRequired()])


class BlogForm(FlaskForm):
    blog_title = StringField(validators=[DataRequired()])
    blog_content = TextAreaField(validators=[DataRequired()])
    blog_metacontent = StringField(validators=[DataRequired()])
    blog_writer = StringField(validators=[DataRequired()])
    blog_image = StringField(validators=[DataRequired()])
    blog_date = StringField(validators=[DataRequired()])
