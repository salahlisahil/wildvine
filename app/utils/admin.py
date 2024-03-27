from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.models.models import Event, Views, db

admin = Admin(name='Wild', template_mode='bootstrap4')

admin.add_view(ModelView(Event, db.session))
admin.add_view(ModelView(Views, db.session))