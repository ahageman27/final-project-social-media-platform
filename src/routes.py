
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from src import app, db, load_user
from forms import *
from models import *

# Route for handling the login page logic
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():

    login_form = LoginForm()
    if request.method == 'POST' and login_form.validate_on_submit():

        user = db.session.query(User).filter(User.name==login_form.username.data).first()

        if user and user.password_hash == login_form.password.data:
            login_user(user)
            return redirect(url_for('dashboard'))
    
    return render_template('login.html', login_form=login_form)

# Route for handling the logout page logic
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

# Route for handling the registeration page logic
@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if request.method == 'POST' and register_form.validate_on_submit():

        user = db.session.query(User).filter(User.name==register_form.username.data).first()
        if user:
            return redirect(url_for('register'))
        
        user = User(
            name = register_form.username.data,
            password_hash = register_form.password.data
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('register.html', register_form=register_form)

# Route for handling the dashboard page logic
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/chat')
@login_required
def chat():
    return render_template('chat.html')

@app.route('/post')
@login_required
def post():
    return render_template('post.html')

@app.route('/About')
def about():
    return render_template('About_Us.html')
