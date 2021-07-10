from flask_wtf import form
from . import admin
from flask import render_template, session , flash , redirect , url_for , request , abort
from .utils import admin_only_view
from mod_mahsolat.forms import MahsolatForms 
from mod_mahsolat.models import Mahsolat
from app import db

@admin.route('/', methods=['GET', 'POST'])
@admin_only_view
def index():
    # form = MahsolatForms()
    return render_template('admin/index.html')



@admin.route('/mahsolat/' ,methods=['GET', 'POST'])
@admin_only_view
def mahsolat():
    if not session.get('email'):
        flash('شما حساب کاربری ندارید. ابتدا در این صفحه وارد حساب کاربری تان شوید',category='bg-danger')
        return redirect(url_for('users.login'))
    
    all_mahsolat = Mahsolat.query.order_by(Mahsolat.id.desc()).all()
    # .filter(Mahsolat.username == session.get('username'))
    return render_template('admin/mahsolat.html' , form = form , all_mahsolat = all_mahsolat)



@admin.route('/create_mahsol/' , methods=['GET', 'POST'])
@admin_only_view
def create_mahsol():
    form = MahsolatForms() 
    if request.method == 'POST':
        if not session.get('email'):
            flash(' شما حساب کاربری ندارید. ابتدا در این صفحه وارد حساب کاربری تان شوید', category='bg-danger')
            return redirect(url_for('users.login')) 
        session['mahsol_title'] = request.form.get('mahsol_title')    
        session['mahsol_category'] = request.form.get('mahsol_category')
        session['mahsol_price'] = request.form.get('mahsol_price')
    
    
        if not session.get('mahsol_title'):
            flash('لطفا فرم را کامل پر کنید', category='bg-danger')
            return render_template('admin/mahsolat.html' , form = form)
    
        if not session.get('mahsol_category'):
            flash('لطفا فرم را کامل پر کنید', category='bg-danger')
            return render_template('admin/mahsolat.html' , form = form)

    
        if not session.get('mahsol_price'):
            flash('لطفا فرم را کامل پر کنید', category='bg-danger')
            return render_template('admin/mahsolat.html' , form = form)

        # print(session.get("mahsol_title"))
        # print(session.get("mahsol_category"))
        # print(session.get("mahsol_price"))


        # new_mahsol = Mahsolat()
        # new_mahsol.title = form.mahsol_title.data
        # new_mahsol.description = form.mahsol_description.data
        # new_mahsol.group = form.mahsol_category.data
        # new_mahsol.price = form.mahsol_price.data
        # new_mahsol.image = form.mahsol_image.data
        # db.session.add(new_mahsol)
        # db.session.commit()


    return render_template('admin/create_mahsol.html' , form = form)


@admin.route('/register_mahsol/', methods=['GET', 'POST'])
@admin_only_view
def register_mahsol():
    form = MahsolatForms()
    if request.method == 'POST':
        if not session.get('email'):
            flash(' شما حساب کاربری ندارید. ابتدا در این صفحه وارد حساب کاربری تان شوید', category='bg-danger')
            return redirect(url_for('users.login')) 
        new_mahsol = Mahsolat()
        new_mahsol.title = form.mahsol_title.data
        new_mahsol.description = form.mahsol_description.data
        new_mahsol.group = form.mahsol_category.data
        new_mahsol.price = form.mahsol_price.data
        new_mahsol.image = form.mahsol_image.data
        new_mahsol.slug = form.mahsol_title.data
        db.session.add(new_mahsol)
        db.session.commit()
        print(form.mahsol_image.data)
        flash('محصول با موفقیت ثبت شد', category='bg-success')
        return redirect(url_for('admin.mahsolat'))

    return render_template('admin/create_mahsol.html' , form = form)


@admin.route('/<string:slug>')
@admin_only_view
def single_mahsol(slug):
    mahsol = Mahsolat.query.filter(Mahsolat.slug == slug).first_or_404()
    # mahsol_name = File.query.filter(File.project_name == project.project_name)
    return render_template('admin/single_mahsol.html' , mahsol=mahsol )