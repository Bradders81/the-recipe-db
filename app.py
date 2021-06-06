import os
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("index.html")


@app.route("/recipes")
def recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email_registered = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if email_registered:
            flash("Email address already registered.")
            return redirect(url_for("signup"))

        create_account = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(create_account)

        session["new_user"] = request.form.get("username").lower()
        flash("Your Profile has been created.")
        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("email").lower()
                    flash("You are now Logged in")
            else:
                flash("Incorrect login details, please try again.")
                return redirect(url_for("login"))

        else:
            flash("Incorrect login details, please try again.")
            return redirect(url_for("login"))

    return render_template("login.html")


@ app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
