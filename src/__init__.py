
from flask import Flask

app = Flask(__name__)
app.secret_key = 'do not share your sercret key'

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@db:3306/mysql'
db.init_app(app)

import models
with app.app_context(): 
    db.create_all()

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# user_loader callback
@login_manager.user_loader
def load_user(name):
    try: 
        return db.session.query(models.User).filter(models.User.name==name).one()
    except: 
        return None

import routes
