from . import mahsolat
from flask import session , flash , request , redirect ,url_for,render_template
from .forms import MahsolatForms

@mahsolat.route('/')
def index():
    pass




