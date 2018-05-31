from wtforms import (Form, StringField, DateTimeField, SubmitField, PasswordField,
                     validators as v)
from wtforms.widgets import TextArea


class ReminderForm(Form):
    message = StringField("Message", validators=[v.length(min=1, max=160),
                        v.InputRequired()], widget=TextArea())
    send_on = DateTimeField("Send On", validators=[
        v.InputRequired()], format='%Y/%m/%d %H:%M')
    submit = SubmitField('Create')


class LoginForm(Form):
    email = StringField('Email', validators=[v.InputRequired(), v.Email()])
    password = PasswordField('Password', validators=[v.InputRequired()])
    #password2 = PasswordField('Repeat password', validators=[v.InputRequired(),
    #thi is for registration               v.EqualTo('password')])
    submit = SubmitField('Login')