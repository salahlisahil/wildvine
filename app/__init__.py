from flask import Flask

from app.models.models import db
from app.routes import index_bp
from app.utils import sessions, mail, admin

app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(index_bp)

sessions.init_app(app)
mail.init_app(app)
admin.init_app(app)
