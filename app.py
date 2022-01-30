from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
### Database Stuff ###
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Registry(db.Model):
    apptype = db.Column(db.String, primary_key=True) ## New, Change in Address/Location in County, Replacement Voter Card
    interestelectionw = db.Column(db.Integer, unique=True, nullable=False) ## Yes/No
    firstName = db.Column(db.String(120), unique=True, nullable=False)
    middleName = db.Column(db.String(120), unique=True, nullable=True) #optional
    lastName = db.Column(db.String(120), unique=True, nullable=False) # including suffix
    formerName = db.Column(db.String(120), unique=True, nullable=True) #optional
    DOB = db.Column(db.String(120), unique=True, nullable=False) ## mm/dd/yyyy
    gender = db.Column(db.String(120), unique=True, nullable=True) ## male/female
    phonenumber = db.Column(db.String(10), unique=True, nullable=True) ## areacode:3, middle:3, last: 4 try to split
    dln = db.Column(db.String(8), unique=True, nullable=False) ## drivers license num
    ssn4 = db.Column(db.String(4), unique=True, nullable=False) ## or last 4 of ssn
    resAddress = db.Column(db.String(120), unique=True, nullable=False) ##
    resCounty = db.Column(db.String(120), unique=True, nullable=False)
    resZip = db.Column(db.String(9), unique=True, nullable=False) ## first 5, last 4 SPLIT
    formerCityCounty = db.Column(db.String(120), unique=True, nullable=False) ## Austin, Travis
    mailingAddress = db.Column(db.String(120), unique=True, nullable=False) ## Address, City
    mailing = db.Column(db.String(120), unique=True, nullable=True) ## if res is not mailing addy format: Address, City, State, two box zip

    def __repr__(self):
        return '<User %r>' % self.username


#######

### Routes ###

@app.route('/')
def home():
    return render_template('Page_1.html')

@app.route("/register")
def register():
    return render_template('2ndpage.html');



#######

if __name__ == "__main__":
    app.run(debug=True)
