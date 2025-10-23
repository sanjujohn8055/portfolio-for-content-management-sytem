from flask import Blueprint, render_template, redirect, url_for, flash, request
from .forms import LoginForm, SignupForm
from .models import User, Project
from . import db
from flask_login import login_user, logout_user, login_required, current_user

auth_bp = Blueprint('auth', __name__, template_folder='templates')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.admin_dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.admin_dashboard'))
        flash('Invalid username or password', 'danger')
    return render_template('admin/login.html', form=form)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.admin_dashboard'))
    
    form = SignupForm()
    if form.validate_on_submit():
        # Check if username already exists
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'danger')
            return render_template('admin/signup.html', form=form)
        
        # Check if email already exists
        existing_email = User.query.filter_by(email=form.email.data).first()
        if existing_email:
            flash('Email already registered. Please use a different email.', 'danger')
            return render_template('admin/signup.html', form=form)
        
        # Create new user
        user = User(
            username=form.username.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('admin/signup.html', form=form)



@auth_bp.route('/guest')
def guest_login():
    """Allow users to explore as a guest without creating an account"""
    # Create or get the guest user
    guest_user = User.query.filter_by(username='guest').first()
    if not guest_user:
        guest_user = User(
            username='guest',
            email='guest@portfolio.demo'
        )
        guest_user.set_password('guest123')  # Guest needs a password for the model
        db.session.add(guest_user)
        db.session.commit()
    
    login_user(guest_user)
    flash('Welcome! You are exploring as a guest. Create an account to save your changes.', 'info')
    return redirect(url_for('main.admin_dashboard'))

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
