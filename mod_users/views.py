from itertools import count
from flask import request , render_template , flash , session , abort , redirect , url_for
from . import users
from .models import User 
from .forms import RegisterForm , LoginForm
from app import db
from mod_mahsolat.models import Mahsolat
from mod_users.models import Blogs


@users.route('/')
def index():
    pass




@users.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash('لطفا تمامی فیلدها را پر کنید' , 'bg-danger')
            return render_template('users/register.html', form=form)
        if not form.password.data == form.confirm_password.data:
            flash('رمز عبور وتکرار رمز عبور مطابقت ندارد' , 'bg-danger')
            return render_template('users/register.html', form=form)
        
        phone_number_int = len(f"{form.phone_number.data}")
        if not phone_number_int >= 10:
            flash('شماره تلفن صحیح نیست!' , 'bg-danger')
            return render_template('users/register.html', form=form)
        old_username = User.query.filter(User.username.ilike(form.username.data)).first()
        if old_username:
            flash('نام کاربری تکراری میباشد' , 'bg-danger')
            return render_template('users/register.html', form=form)

        old_user = User.query.filter(User.email.ilike(form.email.data)).first()
        if old_user:
            flash('ایمیل تکراری می باشد' , 'bg-danger')
            return render_template('users/register.html', form=form)

        

        new_user = User()
        new_user.username = form.username.data
        new_user.email = form.email.data
        new_user.set_password(form.password.data)
        new_user.phone_number = form.phone_number.data
        db.session.add(new_user)
        db.session.commit()
        print(form.username.data)
        flash('ثبت نام با موفقیت انجام شد' , 'bg-success')
        return redirect(url_for('users.login'))
        # except IntegrityError:
        #     db.session.rollback()
        #     flash('Email is in use.' , 'bg-danger')
    return render_template('users/register.html', form=form)










@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash('لطفا تمامی فیلدها را پر کنید' , 'bg-danger')
            return render_template('users/login.html', form=form)
        user = User.query.filter(User.email.ilike(f"{form.email.data}")).first()

        if not user:
            flash("نام کاربری / رمز ورود  نادرست است", category='bg-danger')
            return render_template('users/login.html', form=form)

        if not user.check_password(form.password.data):
            flash("نام کاربری / رمز ورود  نادرست است", category='bg-danger')
            return render_template('users/login.html', form=form)
        
        # if user:
        #     flash("شما از قبل وارد شده اید", category='bg-danger)
        #     return(redirect(url_for('index')))
        
        session['email'] = user.email
        session['user_id'] = user.id
        session['username'] = user.username
        session['role'] = user.role
        

        if user.role == 1:
            flash("ورود با موفقیت انجام شد", category='bg-success')
            return redirect(url_for('admin.index'))

        # return redirect(url_for('index'))
    
    if session.get('role') == 1:
        flash("ورود با موفقیت انجام شد", category='bg-success')
        return redirect(url_for('admin.index'))
    
    if session.get('email') is not None:
        flash("ورود با موفقیت انجام شد", category='bg-success')
        return redirect(url_for('index'))
    

    return render_template('users/login.html', form=form)












@users.route('/logout/', methods = ['GET'])
def logout():
    if session.get('email'):
        session.clear()
        flash('با موفقیت خارج شدید' , 'bg-warning')
        return(redirect(url_for('users.login')))
        
    flash('شما وارد نشده اید' , 'bg-warning')
    return(redirect(url_for('users.login')))

@users.route('/<string:slug>')
def single_mahsol(slug):
    mahsol = Mahsolat.query.filter(Mahsolat.slug == slug).first_or_404()
    # mahsol_name = File.query.filter(File.project_name == project.project_name)
    all_mahsolat = Mahsolat.query.order_by(Mahsolat.id.desc()).all()
    return render_template('users/single_mahsol.html' , mahsol=mahsol , all_mahsolat=all_mahsolat)

@users.route('/<string:slug>/')
def single_blog(slug):
    single_blog = Blogs.query.filter(Blogs.slug == slug).first_or_404()
    return render_template('admin/single_blog.html' , single_blog=single_blog )