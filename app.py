from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import json
import os


app = Flask(__name__)
Bootstrap(app)


### Database Stuff ###
app.secret_key = b'noRussian'
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
    return render_template('homepage.html')

@app.route('/vreg')
def register():
    return render_template('registertovote.html')

@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        jsonFile = "view.json" ## tests.json
        form_data = request.form.to_dict(flat=False)
        try:
            with open(jsonFile, 'a') as f:
                json.dump(form_data, f)
        except:
            with open(jsonFile, 'w') as d:
                json.dump(form_data, d)

        return render_template('data.html',form_data = form_data)

@app.route('/view')
def test():
    title = "View your information" ## Tests
    with open('view.json') as json_file:
        dict_data = json.load(json_file)
    json_file.close()   
    return render_template('view.html', title=title, data=dict_data)





#######

if __name__ == "__main__":
    app.run(debug=True)