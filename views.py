from app import app
from mod_mahsolat.models import Mahsolat , MahsolGroups
from flask import render_template


@app.route('/')
def index():
    all_mahsolat = Mahsolat.query.order_by(Mahsolat.id.desc()).all()
    groups = MahsolGroups.query.order_by(MahsolGroups.id.desc()).all()
    return render_template('index.html' , all_mahsolat = all_mahsolat , groups=groups)


