from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app
from flask_admin import Admin


db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
admin = Admin(app, name='bankrespublika', template_mode='bootstrap3')