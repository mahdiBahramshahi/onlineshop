from mod_admin.views import mahsolat
from app import app
from mod_mahsolat.models import Mahsolat , MahsolGroups
from flask import render_template


@app.route('/')
def index():
    all_mahsolat = Mahsolat.query.order_by(Mahsolat.id.desc()).all()
    groups = MahsolGroups.query.order_by(MahsolGroups.id.desc()).all()
    return render_template('index.html' , all_mahsolat = all_mahsolat , groups=groups)

@app.route('/<string:slug>')
def single_group(slug):
    singlegroup = MahsolGroups.query.filter(MahsolGroups.title == slug).first_or_404()
    mahsolat= Mahsolat.query.filter(Mahsolat.group == slug).all()
    return render_template('users/single_group.html' , singlegroup=singlegroup , mahsolat=mahsolat )
