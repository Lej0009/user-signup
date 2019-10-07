from flask import Flask, render_template, request, redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True



# look inside the request to figure out what the user typed
username = request.form['username']
password = request.form['password']
verify_password = request.form['verify-pw']

    # if the user typed nothing at all, redirect and tell them the error
if (not username) or (username.strip() == ""):
    error = "Please specify a username."
    return redirect("/?error=" + error)

if (not password) or (password.strip() == ""):
    error = "Please specify a password."
    return redirect("/?error=" + error)

if (not verify_password) or (verify_password.strip() == ""):
    error = "Please verify password."
    return redirect("/?error=" + error)

if password != verify_password:
    error = "Passwords do not match."
    return redirect("/?error=" + error)



@app.route("/")
def index():
    return render_template('base.html')

app.run()