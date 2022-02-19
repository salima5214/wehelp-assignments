import mysql.connector
from flask import Flask, render_template, redirect, session, request, json # jsonify, make_response, url_for

app = Flask(__name__)
app.secret_key = "my_secret_key"


@app.route("/")
def index():
    name = session.get('name')
    if name is not None:
        return redirect("member")
    else:
        return render_template("index.html")

@app.route('/api/members', methods = ['GET'])
def searchMember():
    username = request.args.get('username')
    my_database = mysql.connector.connect(
            host = "localhost",
            database = "website",
            user = "root",
            password = "12345678"
        )
    cursor = my_database.cursor()
    my_command = "SELECT id, name, username FROM member WHERE username = %s;"
    cursor.execute(my_command, (username, ))
    user_info = cursor.fetchone()
    if user_info:
        return { "data": { "id": user_info[0], "name": session['name'], "username": user_info[2] } }
    else:
        return { "data": None }


@app.route("/api/member", methods=["POST"]) 
def updateName():
    update_name = request.get_json()
    # print("updateName", updateName) # {'name': 'user_input'}
    update_name = update_name["name"]
    if update_name == "":
        return json.dumps({"error":True})
    else:
        origin_name = session['name']
        my_database = mysql.connector.connect(
                host = "localhost",
                database = "website",
                user = "root",
                password = "12345678"
            )
        cursor = my_database.cursor()      
        cursor.execute("UPDATE member SET name=%(name)s WHERE username=%(username)s", {"name": update_name, "username": origin_name})
        my_database.commit()
        session["name"] = update_name
        return json.dumps({"ok":True})


@app.route("/member")
def member():
    name = session["name"]  # name = session.get("name")
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
    
    my_command = "SELECT name, username, password FROM member WHERE username = '{}';".format(username)
    cursor.execute(my_command)
    user_info = cursor.fetchall()
    cursor.close()
    my_database.close()

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
    my_command = "SELECT username FROM member WHERE username = '{}';".format(username)
    cursor.execute(my_command)
    user_info = cursor.fetchall()
    if user_info == []:
        my_command = "INSERT INTO member (name, username, password) values ('{}', '{}', '{}');".format(name, username, password)
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