from flask import Blueprint


reminders = Blueprint('reminders', __name__, template_folder='templates')


@reminders.route('/')
def hello():
    return "3rd try blue"