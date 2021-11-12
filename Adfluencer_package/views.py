import os
from flask import Blueprint, Response, Flask, session
from flask import request, render_template, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user
from flask import render_template, request
from Adfluencer_package.models import users
from werkzeug.security import generate_password_hash, check_password_hash
from Adfluencer_package import db, create_app, app
from werkzeug.utils import secure_filename
from Adfluencer_package.models import advertisements
from Adfluencer_package.models import advt_approval


app = Flask(__name__)
UPLOAD_FOLDER = 'D:/COLLEGE DOCS/MINI PROJECT SEM-V/AdFluencer/AdFluencer/Adfluencer_package/static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('index.html')


@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pswd')
        user_a = users.query.filter_by(comp_email=email).first()
        user_i = users.query.filter_by(inf_email=email).first()
        if user_a:
            if check_password_hash(user_a.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user_a, remember=True)
                return redirect('/advt/dashboard')
            else:
                flash('Incorrect password, try again.', category='error')

        elif user_i:
            if check_password_hash(user_i.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user_i, remember=True)
                return redirect('/infl/dashboard')
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist', category='error')
    return render_template('login.html')


@views.route('/logout')
@login_required
def logout():
    logout_user()
    flash("logged out successfully!", category='success')
    return redirect(url_for('views.home'))


@views.route('/advt/dashboard', methods = ['GET', 'POST'])
@login_required
def advt_dashboard():
    if current_user.comp_name == None:
        flash('Please login')
        return redirect(url_for('views.login'))
    else:
        name = current_user.comp_name
        owner_id = current_user.id
        advts_owner= advertisements.query.all()
        advts = advertisements.query.filter_by(owner_id=owner_id)
        advts_oid = advertisements.query.filter_by(owner_id=owner_id).first()
        try:
            adv_oid = advts_oid.owner_id
            return render_template('advt_dashboard.html',advts=advts, name=name, advts_owner=advts_owner, adv_oid=adv_oid, owner_id=owner_id)
        except:
            pass
        return render_template('advt_dashboard.html',advts=advts, name=name, advts_owner=advts_owner, owner_id=owner_id)


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@views.route('/advt/advertise', methods = ['GET', 'POST'])
@login_required
def advt_advertise():
    if current_user.comp_name == None:
        flash('Please login')
        return redirect(url_for('views.login'))
    else:
        if request.method == 'POST':
            files = request.files.getlist('prdt_imgs')
            for file in files:
                if file and allowed_file(file.filename):
                    comp_name = current_user.comp_name
                    email = current_user.comp_email
                    desc = request.form.get('desc')
                    brand = request.form.get('brand')
                    deadline = request.form.get('deadline')
                    prdt_sp = request.form.get('prdt_sp')
                    age_grp = request.form.get('age_grp')
                    prdt_imgs = request.files['prdt_imgs']
                    owner_id = current_user.id
                    
                    filename = secure_filename(prdt_imgs.filename)
                    mimetype = prdt_imgs.mimetype
                    
                    file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename))
                    advt = advertisements(owner_id=owner_id, comp_name=comp_name, email=email, desc=desc, brand=brand, deadline=deadline, prdt_sp=prdt_sp,
                    age_grp=age_grp, name = filename, mimetype=mimetype)
                    db.session.add(advt)
                    db.session.commit()
                    flash('Advertisement added!', category='success')
                    return redirect(url_for('views.advt_dashboard'))
                else:
                    flash('Please upload a valid image file (JPEG/JPG/PNG/GIF).')
                    user_email=current_user.comp_email
                    comp_name = current_user.comp_name
                    return render_template('advt_advertisements.html',user_email=user_email, comp_name=comp_name)
        
        user_email=current_user.comp_email
        comp_name = current_user.comp_name
        return render_template('advt_advertisements.html', user_email=user_email, comp_name=comp_name)

@views.route('/advt/update_advertise/<int:id>', methods = ['GET', 'POST'])
@login_required
def advt_update(id):
    name_to_update = advertisements.query.filter(advertisements.id==id).first()
    files = request.files.getlist('prdt_imgs')
    for file in files:
        if file and allowed_file(file.filename):                
            name_to_update.desc = request.form.get('desc')
            name_to_update.brand = request.form.get('brand')
            name_to_update.deadline = request.form.get('deadline')
            name_to_update.prdt_sp = request.form.get('prdt_sp')
            name_to_update.age_grp = request.form.get('age_grp')
            name_to_update.prdt_imgs = request.files['prdt_imgs']
            filename = secure_filename(name_to_update.prdt_imgs.filename)  
            name_to_update.name = filename
            try:
                file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename))
                db.session.commit()                    
                flash('Database updated successfully!')
                return redirect(url_for('views.advt_dashboard'))
            except:
                file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename))
                db.session.commit()                    
                flash('Database updated successfully!')
                return redirect(url_for('views.advt_dashboard'))

    advt_id = id
    user_email = current_user.comp_email
    advts = advertisements.query.filter_by(id=advt_id).first()
    return render_template('advt_update_advertisements.html', advts=advts, user_email=user_email, id=advt_id )

@views.route('/advt/delete_advertise/<int:id>')
@login_required
def advt_delete(id):
    advt_to_delete = advertisements.query.get_or_404(id)
    try:
        db.session.delete(advt_to_delete)
        db.session.commit()
        flash('Advertisement deleted successfully!')
        return redirect(url_for('views.advt_dashboard'))
    except:
        flash('some error occured')
        return redirect(url_for('views.advt_dashboard'))
#         try:
    #             infl_id = apply.infl_id
    #         except:
    #             infl_id = None
    # # adv_id = applys.advt_id
    # # owner_id = applys.owner_id
@views.route('/advt/applications/<int:id>', methods = ['GET', 'POST'])
@login_required
def advt_apply(id):
    advt_id = id
    # user_email = current_user.comp_email
    ap=advt_approval.query.all()
    apl = advt_approval.query.filter_by(advt_id=advt_id, approved=0).all()    
    # applys = advt_approval.query.filter_by(approved=0).all()
    # for item in applys:
    #     infl_id = item.infl_id
    # infl_int = users.query.filter_by(id=infl_id)
    advts = advertisements.query.filter_by(id=advt_id).first()
    return render_template('advt_applications.html', advt=advts,apl=apl,ap=ap )

        # flash('some error occured')
    # advts = advertisements.query.filter_by(id=advt_id).first()
    # return render_template('advt_applications.html', advt=advts, applys=applys,apl=apl )


@views.route('/advt/approved_applications/<int:id>', methods = ['GET', 'POST'])
@login_required
def advt_app_applicants(id):
    advt_id = id
    # user_email = current_user.comp_email
    apl = advt_approval.query.filter_by(advt_id=advt_id).first()
    applys = advt_approval.query.all()
    for apply in applys:
        if apply.approved==1:
            try:
                infl_id = apply.infl_id
            except:
                flash('some error occured')
                # infl_id = None
    # adv_id = applys.advt_id
    # owner_id = applys.owner_id
    try:
        infl_int = users.query.filter_by(id=infl_id)
        advts = advertisements.query.filter_by(id=advt_id).first()
        return render_template('advt_approved_applicants.html', advt=advts, applys=applys, infl_int=infl_int,apl=apl )
    except:
        flash('some error occured')
    advts = advertisements.query.filter_by(id=advt_id).first()
    return render_template('advt_approved_applicants.html', advt=advts, applys=applys,apl=apl )


@views.route('/advt/applications/approve/<int:id>', methods = ['GET', 'POST'])
@login_required
def advt_approve(id):
    infl_id = id
    advt_apr = advt_approval.query.filter_by(infl_id=infl_id).first()
    advt_apr.approved=1
    advt_apr.filter='approved'
    
    db.session.commit()
    flash('Influencer application approved! Hope you have a great collaboartion!')
    return redirect(url_for('views.advt_dashboard'))


@views.route('/advt/applications/reject/<int:id>')
@login_required
def advt_reject(id):
    apply_to_delete = advt_approval.query.get_or_404(id)
    try:
        db.session.delete(apply_to_delete)
        db.session.commit()
        flash('Application rejected, hope you find a better candidate!')
        return redirect(url_for('views.advt_dashboard'))

    except:
        flash('some error occured ')
        return redirect(url_for('views.advt_dashboard'))

@views.route('/advt/advt_details/<int:advt_id>', methods = ['POST', 'GET'])
@login_required
def advt_details(advt_id):
    advt = advertisements.query.filter_by(id=advt_id).first()
    return render_template('advt_details.html', advt=advt)


@views.route('/infl/dashboard', methods = ['POST', 'GET'])
@login_required
def infl_dashboard():
    if request.method == 'POST':
        advt_id = request.form.get("advt_id")
        owner_id = request.form.get("owner_id")
        owner_name = request.form.get("owner_name")
        infl_id = request.form.get("infl_id")
        infl_fname = request.form.get("infl_fname")
        infl_lname = request.form.get("infl_lname")
        infl_smh = request.form.get("infl_smh")
        infl_email = request.form.get("infl_email")
        filter='applied'
        apply = advt_approval(advt_id = advt_id, owner_id = owner_id, owner_name=owner_name, infl_id = infl_id, infl_fname=infl_fname, infl_lname=infl_lname, infl_smh=infl_smh, infl_email=infl_email,filter=filter)
        db.session.add(apply)
        db.session.commit()
        name = current_user.fname
        advts= advertisements.query.all()
        return render_template('infl_dashboard.html', name=name, advts=advts)
    else:
        if current_user.fname == None:
            flash('Please login')
            return redirect(url_for('views.login'))
        else:
            name = current_user.fname
            advts= advertisements.query.all()
            return render_template('infl_dashboard.html', name=name, advts=advts)


@views.route('/infl/portfolio_details<int:advt_id>', methods = ['POST', 'GET'])
@login_required
def portfolio_details(advt_id):
    advt = advertisements.query.filter_by(id=advt_id).first()
    return render_template('infl_portfolio.html', advt=advt)

@views.route('/infl/my_profile/portfolio_details<int:advt_id>', methods = ['POST', 'GET'])
@login_required
def my_portfolio_details(advt_id):
    advt = advertisements.query.filter_by(id=advt_id).first()
    return render_template('my_infl_portfolio.html', advt=advt)


@views.route('/infl/my_profile')
@login_required
def my_profile():
    
    apl = advt_approval.query.all()
    infl_id=current_user.id
    advt_apl = advt_approval.query.filter_by(infl_id=infl_id).first()
    user= users.query.filter_by(id=infl_id).first()
    try:
        advt_id = advt_apl.advt_id    
        advts_apl = advertisements.query.filter_by(id=advt_id)
        advts_apl_inf = advt_approval.query.filter_by(id=advt_id).first()
        inf_id=advts_apl_inf.infl_id
        return render_template('infl_profile.html', advts = advts_apl, apl=apl, advt_id=advt_id, advt_apl=advt_apl, user=user,inf_id=inf_id, infl_id=infl_id)
    except:
        return render_template('infl_profile.html',  apl=apl, advt_apl=advt_apl, user=user, infl_id=infl_id)

@views.route('/register')
def register():
    return render_template('registration.html')


@views.route('/adv_regis', methods=['GET', 'POST'])
def adv_regis():
    if request.method == 'POST':
        comp_name = request.form.get("comp_name")
        acc_handler_name = request.form.get("acc_handler_name")
        acc_handler_desig = request.form.get("acc_handler_desig")
        comp_website = request.form.get("comp_website")
        ph_no = request.form.get("ph_no")
        comp_email = request.form.get("comp_email")
        ah_email = request.form.get("ah_email")
        pswd1 = request.form.get("pswd1")
        acc_handler_gender = request.form["gender"]
        acc_type = 'advt'
        
        user = users.query.filter_by(comp_email=comp_email).first()
        if user:
            flash('Email already exists.', category='error')
            return render_template('advertiser-registration.html')
        else:
            hashed_password = generate_password_hash(
                pswd1, method='sha256')
            adv_regis_user = users(comp_name=comp_name, acc_handler_name=acc_handler_name,
            acc_handler_desig=acc_handler_desig, comp_website=comp_website, ph_no=ph_no, comp_email=comp_email,
            ah_email=ah_email, password=hashed_password, acc_handler_gender=acc_handler_gender, acc_type=acc_type)
            db.session.add(adv_regis_user)
            db.session.commit()
            flash('Account created! Please login', category='success')
            return redirect(url_for('views.login'))
    return render_template('advertiser-registration.html')


@views.route('/inf_regis', methods=['GET', 'POST'])
def inf_regis():
    if request.method == 'POST':
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        smh = request.form.get("smh")
        ph_no = request.form.get("ph_no")
        inf_email = request.form.get("inf_email")
        age = request.form.get("age")
        pswd1 = request.form.get("pswd1")
        gender = request.form["gender"]
        acc_type = 'infl'

        user = users.query.filter_by(inf_email=inf_email).first()
        if user:
            flash('Email already exists.', category='error')
            return render_template('influencer-registration.html')
        else:
            hashed_password = generate_password_hash(
                pswd1, method='sha256')
            inf_regis_user = users(fname=fname, lname=lname, smh=smh,ph_no=ph_no, 
            inf_email=inf_email, password=hashed_password, age=age, gender=gender, acc_type=acc_type)
            db.session.add(inf_regis_user)
            db.session.commit()
            flash('Account created! Please login', category='success')
            return redirect(url_for('views.login'))
    return render_template('influencer-registration.html')
