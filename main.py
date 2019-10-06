import flask from flask

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE HTML>
<html>
    <head>

    </head>

    <body>
        <h1>Signup</h1>

        <form action = "/" methods = "POST">
            Username <input type="text" name="username" value="">
            Password <input type="text" name="password" value="">
            Verify Password <input type="text" name="verify_password" value="">
            Email (optional) <input type="text" name="email" value="">
            <input type="submit"></input>
        </form>

    </body>
</html>