from flask import Flask, render_template, request, redirect
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True

# look inside the request to figure out what the user typed
# username = request.form['username']
# password = request.form['password']
# verify_password = request.form['verify-password']
# email = request.form['email']


# password_error = ''
# verify_password_error = ''
# email_error = ''


def username_error(username):
    space = False
    for char in username:
        if char.isspace() == True:
            space = True
    

    if 2 < len(username) < 20 and space == False :
        return False
    else:
        return True

def password_error(password):
    space = False
    for char in password:
        if char.isspace() == True:
            space = True
    
    if 2<len(password)<20 and space == False:
        return False
    else:
        return True

def verify_error(verify, password):
    if verify == password:
        return False
    else:
        return True

def email_error(email):
    if "@" in email and "." in email and " " not in email and 2<len(email)<20:
        return False
    else:
        return True


@app.route("/")
def index():
    return render_template('base.html', username='', username_error='', password='', password_error='', verify='', verify_password_error='')

@app.route("/signup", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    error = ''
  
    if not username_error(username) and not password_error(password) and not verify_error(verify, password) and not email_error(email):
        return render_template('welcome.html', username=username)

    
    if username_error(username):
        error = "Please specify a username that is between 3 and 20 characters and contains no spaces."
        username = ''
        return render_template('base.html',username_error = error)

    if password_error(password):
        error = "Please specify a password that is between 3 and 20 characters and contains no spaces."
        password = ''
        return render_template('base.html', password_error = error)

    if verify_error(verify, password):
        error = "Passwords do not match."
        return render_template('base.html', password_error=error, verify_password_error=error)

    if email_error(email):
        error = "Please specify a valid email."
        email = ''
        return render_template('base.html', email_error=error)

       

app.run()



#     # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
#     username_escaped = cgi.escape(username, quote=True)
#     password_escaped = cgi.escape(password, quote=True)
#     verify_password_escaped = cgi.escape(verify_password, quote=True)
#     email_escaped = cgi.escape(email, quote=True)



