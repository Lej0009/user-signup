from flask import Flask, render_template, request, redirect
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

# look inside the request to figure out what the user typed
username = request.form['username']
password = request.form['password']
verify_password = request.form['verify-password']
email = request.form['email']

def validate_username():
    #username must be between 3 and 20 characters
    if 3 < len(username) < 20:
        return True
    else:
        return False



@app.route("/")
def index():
    return render_template('base.html')

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

