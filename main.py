from flask import Flask, render_template, request, redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    return render_template('base.html')

app.run()