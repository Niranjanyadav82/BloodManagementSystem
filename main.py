from flask import Flask, render_template, request, session, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "99009"

client = MongoClient("mongodb://localhost:27017/")
db = client["blood_db"]
blood_collection = db["blood"]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/find_blood")
def find_blood():
    bloodgroup = request.args.get("bloodgroup")
    rows = blood_collection.find({"bloodgroup": bloodgroup}) if bloodgroup else []
    return render_template("find_donor.html", rows=rows)


# Blood-group search form ke liye GET endpoint
@app.route("/homeblood")
def home_blood():
    bloodgroup = request.args.get("bloodgroup")
    rows = blood_collection.find({"bloodgroup": bloodgroup}) if bloodgroup else []
    return render_template("find_blood.html", rows=rows)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login_verify", methods=["POST"])
def verify():
    username = request.form.get("username")
    password = request.form.get("password")

    donor = blood_collection.find_one({
        "username": username,
        "password": password
    })

    if donor:
        session["u"] = username
        session["w"] = "owner"
        return render_template("display.html", donordetails=donor)

    return render_template("login.html", res="Invalid username or password")


@app.route("/passdb", methods=["POST"])
def pass_db():
    blood_collection.insert_one({
        "username": request.form.get("username"),
        "password": request.form.get("password"),
        "name": request.form.get("fullname"),
        "dob": request.form.get("dob"),
        "gender": request.form.get("gender"),
        "bloodgroup": request.form.get("bloodgroup"),
        "pno": request.form.get("mobile"),
        "email": request.form.get("email"),
        "town": request.form.get("town"),
        "city": request.form.get("state")
    })

    return render_template("register.html", resultCode="Stored Successfully")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/hello")
def hello():
    return redirect(url_for("register"))


if __name__ == "__main__":
    app.run(debug=True)