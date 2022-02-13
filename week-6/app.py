import mysql.connector
from flask import Flask, render_template, redirect, session, request # url_for

app = Flask(__name__)
app.secret_key = "my_secret_key"


@app.route("/")
def index():
    name = session.get('name')
    if name is not None:
        return redirect("member")
    else:
        return render_template("index.html")


@app.route("/member")
def member():
    name = session.get('name')
    if name is not None:
       return render_template("member.html", name = name)
    else:
        return redirect("/")


@app.route("/error/")
def error():
    user_message = request.args.get("message") 
    return render_template("error.html", message = user_message)


@app.route("/signin", methods = ["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]

    my_database = mysql.connector.connect(
            host = "localhost",
            database = "website",
            user = "root",
            password = "12345678"
        )
    cursor = my_database.cursor()
    
    my_command = "select name, username, password from member where username = '{}';".format(username)
    cursor.execute(my_command)
    user_info = cursor.fetchall()
    cursor.close()
    my_database.close()

    # print("user_info", user_info) # [(name, username, password)]
    # print("user_info[0]", user_info[0]) # (name, username, password)
    # print("user_info[0][0]", user_info[0][0]) # name
    # print("user_info[0][1]", user_info[0][1]) # username
    # print("user_info[0][2]", user_info[0][2]) # password

    if user_info == [] or user_info[0][2] != password:
        user_message = "帳號或密碼輸入錯誤"
        return render_template("error.html", error_message = user_message)       
    else:
        name = user_info[0][0]
        session['name'] = name
        return redirect("member")


        
@app.route("/signup", methods = ["POST"])
def signup():
    name = request.form["name"]
    password = request.form["password"]
    username = request.form["username"]
    password = request.form["password"]
    my_database = mysql.connector.connect(
            host = "localhost",
            database = "website",
            user = "root",
            password = "12345678"
        )
        
    cursor = my_database.cursor()
    my_command = "select username from member where username = '{}';".format(username)
    cursor.execute(my_command)
    user_info = cursor.fetchall()
    if user_info == []:
        my_command = "insert into member (name, username, password) values ('{}', '{}', '{}');".format(name, username, password)
        cursor.execute(my_command)
        my_database.commit()
        cursor.close()
        my_database.close()    
        return redirect("/")
    else:
        user_message = "帳號已經被註冊"
        return render_template("error.html", error_message = user_message)


@app.route("/singout", methods = ["GET"])
def singout():
    session.clear()
    return redirect("/")      


if __name__=="__main__":
    app.run(debug = True, port = 3000)