from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def display_user_signup():
    #template = jinja_env.get_template('user_signup.html')
    return render_template('user_signup.html')

def invalid_user():
    if user == '':
        user_error = "Please choose a name between 3 and 20 letters with no spaces."
        user = ''
    elif len(user) > 20 or len(user) < 3:
        user_error = "Please choose a name between 3 and 20 letters with no spaces."
        user = ''
    else:
        if ' ' in user:
            user_error = "Please remove any spaces."
            user = ''

@app.route('/', methods=['POST'])
def validate_form():

    user = request.form['user']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    user_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    template = jinja_env.get_template('user_signup.html')

    #if empty(user):
    if user == '':
        user_error = "Please choose a name between 3 and 20 letters with no spaces."
        user = ''
    elif len(user) > 20 or len(user) < 3:
        user_error = "Please choose a name between 3 and 20 letters with no spaces."
        user = ''
    else:
        if ' ' in user:
            user_error = "Please remove any spaces."
            user = ''

    if password == '':
        password_error = "Please choose a password between 3 and 20 letters with no spaces."
        password = ''
    elif len(password) > 20 or len(password) < 3:
        password_error = "Please choose a name between 3 and 20 letters with no spaces."
        password = ''
    else:
        if ' ' in password:
            password_error = "Please remove any spaces."
            password = ''

    if password != verify:
        verify_error = "Please re-type your password to verify it."
        verify = ''

    if len(email) == 0:
        email_error = '' 
        email = '' 
    elif len(email) > 20 or len(email) < 3:
        email_error = "Please enter an e-mail address between 3 and 20 letters with no spaces."
        email = ''
    elif ' ' in email:
        email_error = "Please remove any spaces."
        email = ''  
    else:
        at_sign = "@"
        period = "."
        if (not email.count(at_sign) == 1) and (not email.count(period) == 1):
            email_error = "Please type your e-mail address."
            email = ''

    if not user_error and not password_error and not verify_error and not email_error:
        return redirect('/open_sesame?user='+user)
    else:
        return template.render(user=user,user_error=user_error,password_error=password_error,verify_error=verify_error,email_error=email_error)

@app.route('/open_sesame', methods=['GET'])
def open_sesame():
    user = request.args.get('user')

    template = jinja_env.get_template('open_sesame.html')
    return template.render(user=user)

app.run()