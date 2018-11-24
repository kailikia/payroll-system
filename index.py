from flask import Flask,render_template,request,redirect,url_for,flash,session
from employee import Employee
from user import User
from cryptography.fernet import Fernet

app = Flask(__name__)

app.secret_key = "$e$Ce*Tedwin234$"

key = b'ygIpkE1JWf8YvZupVBMSkp2dghsbsYuevnRnTY0B0yU='
cipher_suite = Fernet(key)

def loggedIn():
    if session:
        return True
    return False

@app.route("/auth")
def authentication():
    if loggedIn():
        return redirect(url_for("home"))
    return render_template("register_login.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    confirm = request.form["confirm-password"]
    #Check if password and confirm-password match
    if password != confirm:
        flash("Passwords Do Not Match")
        return redirect(url_for("authentication"))

    #Check if email exist in database
    check = User.select().where(User.email  == email).count()
    if check != 0:
        flash("Email already Exists in our Records")
        return redirect(url_for("authentication"))

    #Encrypt password
    encpass = cipher_suite.encrypt(bytes(password,"utf-8"))

    #IF ALL is okay we create user
    User.create(name=name,email=email,password=encpass)
    session["email"] = email
    flash("You have Successfully Registered")
    return redirect(url_for("home"))

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    #Check if email exists
    check = User.select().where(User.email == email).count()
    if check == 0:
        flash("Wrong Credentials")
        return redirect(url_for("authentication"))
    else:
        user = User.select().where(User.email == email).get()
        passwordFromDb = cipher_suite.decrypt(bytes(user.password,"utf-8")).decode("utf-8")
        # Compare if paswordType == password DB
        if password == passwordFromDb:
            #login is okay set session and redirect home
            session["email"] = email
            flash("Successfully Logged in")
            return redirect(url_for("home"))
        else:
            flash("Wrong Credentials")
            return redirect(url_for("authentication"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("authentication"))

@app.route("/")
def home():
    if loggedIn():
        allEmployees = Employee.select()
        return render_template("index.html", displayEmployees = allEmployees)
    return redirect(url_for("authentication"))

@app.route("/employee")
def employee():
    return render_template("addEmployee.html")

@app.route("/saveEmployee",methods=["POST"])
def saveEmployee():
    name = request.form["hp"]
    #
    # Employee.create(full_name= request.form['form_full_name'],
    #                 kra_pin_number=kra,
    #                 department='ICT',
    #                 position='Systems Analyst',
    #                 basic_salary=50000,
    #                 house_allowance=60000)
    return name



if __name__ == "__main__":
    app.run(debug=True, port=5005)