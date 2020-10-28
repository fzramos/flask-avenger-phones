from avengers_app import app

from flask import render_template

from avengers_app.forms import UserInfoForm

@app.route('/')
def home():
    return render_template('home.html')

# GET == Gathering info
# POST == Sending info
@app.route('/register', methods = ['GET', 'POST'])
def register():
    # Init our form
    form = UserInfoForm()
    return render_template('register.html', user_form = form)