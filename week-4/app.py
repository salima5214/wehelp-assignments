
from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)


app.secret_key = "my_secret_key"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/member")
def member():
    if session["is_login"] == True:
        return render_template("member.html")
    else:
        return redirect("/")      

@app.route("/error")
def error():
    user_message = request.args.get("message", "") 
    return render_template("error.html", message = user_message)


@app.route("/signin", methods = ["POST"])
def signin():
    account = request.form["account"]
    password = request.form["password"]

    if account == "test" and password == "test":
        session["is_login"] = True
        return redirect("/member")

    elif account == "" or password == "":
        user_message = "請輸入帳號、密碼"
        return redirect(f"/error?message={user_message}")

    else:
        user_message = "帳號、或密碼輸入錯誤"
        return redirect(f"/error?message={user_message}")


@app.route("/signout/")
def signout():
    session["is_login"] = False
    return redirect("/")

app.run(port = 3000)
