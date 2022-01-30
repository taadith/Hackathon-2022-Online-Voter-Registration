from optparse import Values
from tkinter import INSERT
from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange, DataRequired
from datetime import date

app = Flask(__name__)
Bootstrap(app)


### Database Stuff ###
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


##
db = SQLAlchemy(app)
class reg(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    info = db.Column(db.String(100))

    def __repr__(self):
        return '<Name %r>' % self.name

class infoForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    Email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")
#######

### Routes ###
@app.route('/beep', methods=['GET', "POST"])
def add_info():
    form = infoForm()
    return render_template('.html', form = form)
@app.route('/') ## home page
def home():
    return render_template('page_1.html')

@app.route("/register",  methods =["GET", "POST"]) ## voter registration page
def register():
    
    return render_template('registertovote.html');




#######

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
