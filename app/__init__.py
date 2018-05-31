from flask import Flask
from .views import reminders
from .extensions import db, login_manager, celery
from .models import Reminder, User
from .tasks import send_reminders
from . import celery_config





def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    register_blueprints(app)
    register_extensions(app)
    register_shell(app)



    return app


def register_blueprints(app):
    app.register_blueprint(reminders)


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    celery.init_app(app)

    celery.config_from_object(celery_config)
    login_manager.login_view = 'reminders.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)



def register_shell(app):
    def shell_context():
        return{
            'db': db,
            'Reminder': Reminder,
            'User': User,
            'send_reminders': send_reminders
        }

    app.shell_context_processor(shell_context)

