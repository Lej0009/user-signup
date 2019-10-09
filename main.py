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
    

    if 3 < len(username) < 20 and space == False :
        return False
    else:
        return True

def password_error(password, verify_password):
    space = False
    for char in password:
        for char2 in verify_password:
            if char.isspace() == True:
                space = True
    
    if 3 < len(password) < 20 and 3<len(verify_password)<20 and space == False:
        return False
    else:
        return True


@app.route("/")
def index():
    return render_template('base.html')

@app.route("/signup", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    email = request.form['email']

    error = ''

    if not username_error(username):
        return render_template('welcome.html', username=username)
    else:
        error = "Please specify a username that is between 3 and 20 characters and contains no spaces."
        username = ''
        return render_template('base.html',username_error = error)

    if not password_error(password, verify_password):
        return render_template('welcome.html', password=password, verify_password = password)
    else:
        error = "Please specify a password that is between 3 and 20 characters and contains no spaces."

    if password == verify_password:
        return render_template('welcome.html', password=password, verify_password=verify_password)
    else:
        error = "Passwords do not match."
        

app.run()



# app.route("/", methods=['POST'])
# def verify():
#     # look inside the request to figure out what the user typed
#     username = request.form['username']
#     password = request.form['password']
#     verify_password = request.form['verify-password']
#     email = request.form['email']

#     username_error = ''
#     password_error = ''
#     verify_password_error = ''
#     email_error = ''

#     # if the user typed nothing at all, redirect and tell them the error
#     if (not username) or (username.strip() == ""):
#         username_error = "Please specify a username."


#     if (not password) or (password.strip() == ""):
#         password_error = "Please specify a password."
#         # return redirect("/?error=" + error)

#     if (not verify_password) or (verify_password.strip() == ""):
#         verify_password_error = "Please verify password."
#         # return redirect("/?error=" + error)

#     if password != verify_password:
#         password_match_error = "Passwords do not match."
#         # return redirect("/?error=" + error)


#     # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
#     username_escaped = cgi.escape(username, quote=True)
#     password_escaped = cgi.escape(password, quote=True)
#     verify_password_escaped = cgi.escape(verify_password, quote=True)
#     email_escaped = cgi.escape(email, quote=True)


#     if not username_error and not password_error and not verify_password_error and not email_error:
#         #success message
#     else:
#         return render_template('base.html', username_error, password_error, verify_password_error, password_match_error)

