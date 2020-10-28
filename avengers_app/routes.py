from avengers_app import app

from flask import render_template, request

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

    if request.method == 'POST' and form.validate():
        #Get infor form the form & give them variable names
        name = form.name.data
        phone = form.phone.data
        email = form.email.data
        password = form.password.data
        # print form inputs
        print(name, phone, email, password)

    return render_template('register.html', user_form = form)