from flask_wtf import form
from . import admin
from flask import render_template, session , flash , redirect , url_for , request , abort
from .utils import admin_only_view
from mod_mahsolat.forms import MahsolatForms , MahsolgroupForms
from mod_mahsolat.models import Mahsolat , MahsolGroups
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
    groups = MahsolGroups.query.order_by(MahsolGroups.id).all()
    # .filter(Mahsolat.username == session.get('username'))
    return render_template('admin/mahsolat.html' , form = form , all_mahsolat = all_mahsolat , groups=groups)



@admin.route('/create_mahsol/' , methods=['GET', 'POST'])
@admin_only_view
def create_mahsol():
    form = MahsolatForms() 
    if request.method == 'POST':
        if not session.get('email'):
            flash(' شما حساب کاربری ندارید. ابتدا در این صفحه وارد حساب کاربری تان شوید', category='bg-danger')
            return redirect(url_for('users.login')) 
        
        old_title = Mahsolat.query.filter(Mahsolat.title.ilike(form.mahsol_title.data)).first()
        if old_title:
            flash('نام محصول تکراری میباشد' , 'bg-danger')
            return redirect(url_for('admin.mahsolat'))
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
        

        
    all_mahsolat = Mahsolat.query.order_by(Mahsolat.id.desc()).all()
    groups = MahsolGroups.query.order_by(MahsolGroups.id.desc()).all()

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


    return render_template('admin/create_mahsol.html' , form = form , all_mahsolat = all_mahsolat , groups=groups)


@admin.route('/register_mahsol/', methods=['GET', 'POST'])
@admin_only_view
def register_mahsol():
    form = MahsolatForms()
    if request.method == 'POST':
        if not session.get('email'):
            flash(' شما حساب کاربری ندارید. ابتدا در این صفحه وارد حساب کاربری تان شوید', category='bg-danger')
            return redirect(url_for('users.login')) 
        old_title = Mahsolat.query.filter(Mahsolat.title.ilike(form.mahsol_title.data)).first()
        if old_title:
            flash('نام محصول تکراری میباشد' , 'bg-danger')
            return render_template('admin/mahsolat.html', form=form)
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


@admin.route('/mahsol_groups' , methods=['GET', 'POST'])
@admin_only_view
def mahsol_group():
    groups = MahsolGroups.query.order_by(MahsolGroups.id.desc()).all()
    form = MahsolgroupForms()
    if not session.get('email'):
        flash(' شما حساب کاربری ندارید. ابتدا در این صفحه وارد حساب کاربری تان شوید', category='bg-danger')
        return redirect(url_for('users.login')) 

    
    return render_template('admin/mahsol_group.html' , groups=groups , form=form)




@admin.route('/create_mahsol_groups' , methods=['GET', 'POST'])
@admin_only_view
def create_mahsol_group():
    if not session.get('email'):
        flash(' شما حساب کاربری ندارید. ابتدا در این صفحه وارد حساب کاربری تان شوید', category='bg-danger')
        return redirect(url_for('users.login')) 
    form = MahsolatForms() 


    if request.method == 'POST':
        if not session.get('email'):
            flash(' شما حساب کاربری ندارید. ابتدا در این صفحه وارد حساب کاربری تان شوید', category='bg-danger')
            return redirect(url_for('users.login')) 
        new_group = MahsolGroups()
        new_group.title = request.form.get('group_name')
        new_group.image= request.form.get('group_image')

        db.session.add(new_group)
        db.session.commit()

        flash('محصول با موفقیت ثبت شد', category='bg-success')
        return redirect(url_for('admin.mahsol_group'))

    

    return render_template('admin/mahsol_group.html')

        

@admin.route('/<string:title>')
@admin_only_view
def single_group(title):
    singlegroup = Mahsolat.query.filter(Mahsolat.slug == title).first_or_404()
    return render_template('admin/single_group.html' , singlegroup=singlegroup )





