from mod_admin.views import blogs, mahsolat
from app import app
from mod_mahsolat.models import Mahsolat , MahsolGroups
from flask import render_template
from mod_users.models import Blogs
from mod_mahsolat.forms import SearchForm


@app.route('/')
def index():
    search_form = SearchForm()
    all_mahsolat = Mahsolat.query.order_by(Mahsolat.id.desc()).all()
    groups = MahsolGroups.query.order_by(MahsolGroups.id.desc()).all()
    all_blogs = Blogs.query.order_by(Blogs.id.desc()).all()
    return render_template('index.html' , all_mahsolat = all_mahsolat , groups=groups, all_blogs=all_blogs , search_form=search_form)

@app.route('/<string:slug>')
def single_group(slug):
    singlegroup = MahsolGroups.query.filter(MahsolGroups.title == slug).first_or_404()
    mahsolat= Mahsolat.query.filter(Mahsolat.group == slug).order_by(Mahsolat.id.desc()).all()
    return render_template('users/single_group.html' , singlegroup=singlegroup , mahsolat=mahsolat )
