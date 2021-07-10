from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
from config import Development 
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Development)

db = SQLAlchemy(app)
migrate = Migrate(app , db)


from mod_users import users
from mod_admin import admin
from mod_mahsolat import mahsolat

app.register_blueprint(users)
app.register_blueprint(admin)
app.register_blueprint(mahsolat)

from views import app