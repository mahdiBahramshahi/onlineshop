from flask import Blueprint

mahsolat = Blueprint('mahsolat',__name__,url_prefix='/mahsolat/')

from .models import Mahsolat
from . import views


