from flask import Flask,jsonify,render_template,request,redirect

from controllers.userController  import UserController

app = Flask(__name__)
user_conn = UserController()

@app.route("/")
def home():
    return jsonify("home page")


@app.route("/user")
def user_show():
    users = user_conn.get_users()
    return render_template("list.html" ,users=users)

@app.route("/user/create")
def user_create():
    return render_template("create.html")


@app.route("/user",methods=["POST"])
def user_add():
    data =request.form
    user_conn.add_user(data.get("name"),data.get("phone"),data.get("email"),data.get("age"))
    return redirect("/user")

@app.route("/user_update/<id>")
def user_update_form(id):
    users = user_conn.get_user(id)
    return render_template("edit.html", users = users[0])

@app.route("/user_update/<id>",methods=["POST"])
def user_update(id):
    data =request.form
    user_conn.update_user(data.get("name"),data.get("phone"),data.get("email"),data.get("age"),id)
    return redirect("/user")

@app.route("/user_delete/<id>")
def user_delete(id):
    user_conn.delete_user(id)
    return redirect('/user')

if __name__ == '__main__':
    app.run(debug=True,port = 9000)