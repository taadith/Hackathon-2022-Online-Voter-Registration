from optparse import Values
from tkinter import INSERT
from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


### Database Stuff ###
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

### Form for Registration ###
form_data = {
'key1(field1_name)' : 'value1(field1_value)',
'key2(field2_name)' : 'value2(field2_value)',
}
#####

### Routes ###
@app.route('/home')
def index():
    return render_template('Page_1.html')

@app.route('/vreg')
def register():
    return render_template('registertovote.html')

@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html',form_data = form_data)





#######

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
