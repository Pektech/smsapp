from flask import Blueprint, render_template, flash



reminders = Blueprint('reminders', __name__, template_folder='templates')


@reminders.route('/')
def hello():
    flash("hello world", 'success')
    return render_template('index.html')
