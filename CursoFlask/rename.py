from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError


class ContactForm(Form):
    name = TextField("Name of student", [
                     validators.Required("Please enter your name")])
    Gender = RadioField('Gender', choices = [('M', 'Male'), ('F', 'Female')])
    Address = TextAreaField('Address')
    email = TextField("Email", [validators.Required("Please enter your email"), validators.Email("Please enter your email")])
    Age = IntegerField("age")
    language = SelectField('Languages', choices = [('cpp', 'c++'), ('py', 'Python')])
    submit = SubmitField("Send")