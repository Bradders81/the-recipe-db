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
def home_page():
    """
    Obtains three random recipes from the database to be injected in to
    the jinja for loop to be deplayed as samples of the recipes held in
    the database.
    """
    sample = mongo.db.recipes.aggregate([{"$sample": {"size": 3}}])

    return render_template("index.html", sample=sample)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """
    When the user inputs their details into the sign up
    form this function first checks to see if the username or
    email address is already in use.  If already in use a, massage is
    displayed to the user to let them know. If username and/or email address
    are not in use the account is created and the user is directed to the
    login page
    """
    if request.method == "POST":
        email_registered = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        user_registered = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if user_registered:
            flash("User name not available.")
            return redirect(url_for("signup"))

        if email_registered:
            flash("Email address already registered.")
            return redirect(url_for("signup"))

        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password != confirm_password:
            flash("Passwords do not match")
            return redirect(url_for("signup"))

        create_account = {
            "username": request.form.get("username"),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(create_account)

        session["user"] = request.form.get("username")
        flash("Your Profile has been created.")
        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Works with the login form.  Checks the login details
    entered are correct and logs the user into their account if they are.
    User is automatically directed to their profile page. Uer is alerted if
    they entre the wrong details and is invited to try again
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username")
                flash("You are now Logged in")
                return redirect(url_for("profile"))
            else:
                flash("Incorrect login details, please try again.")
                return redirect(url_for("login"))

        else:
            flash("Incorrect login details, please try again.")

    return render_template("login.html")


@app.route("/logout")
def logout():
    """
    Will log the user out if they are logged in and return them
    to the loggin page.
    """
    if "user" in session:
        session.clear()

    return render_template("login.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    """
    Creates dictionary an the recipe provided by the user
    and stores is in the database.  Once the recipe is stored
    the updated copy of the recipes in the database collection
    are collected from the database and stored in the users_cookbook
    variable and passed to the profile page for rendering.
    """
    if "user" not in session:
        return redirect(url_for("login"))

    username = session["user"]
    users_cookbook = mongo.db.recipes.find({"created_by": username})

    if request.method == "POST":
        new_recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "description": request.form.get("description"),
            "instructions": request.form.get("instructions"),
            "ingredients": request.form.get("ingredients"),
            "cooking_time": request.form.get("cooking_time"),
            "type": request.form.get("type"),
            "created_by": username
        }
        mongo.db.recipes.insert_one(new_recipe)
        flash("Voila! Recipe added to your Cook Book")

    return render_template(
            "profile.html", username=username, users_cookbook=users_cookbook)


@app.route("/profile/<recipe_id>")
def recipe_detail(recipe_id):
    """
    Gets details of the recipe selected by the user from their profile page
    desplays the recipe details on recipe-details.html.  Also obtains the
    user name from the session cookie to display, along with a list of
    all the users recipes for easy access.
    """

    username = session["user"]
    users_cookbook = mongo.db.recipes.find({"created_by": username})
    user_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    return render_template("recipe-details.html", username=username,
                           user_recipe=user_recipe,
                           users_cookbook=users_cookbook)


@app.route("/recipes")
def recipes():
    recipes = mongo.db.recipes.find()

    return render_template("recipes.html", recipes=recipes)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    Gets the details of the recipe of the from the database that the user
    wants to edit and renders the data in the edit form for the user to edit
    and resubmit back to the database collection
    """
    username = session["user"]

    if request.method == "POST":
        update_recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "description": request.form.get("description"),
            "instructions": request.form.get("instructions"),
            "ingredients": request.form.get("ingredients"),
            "cooking_time": request.form.get("cooking_time"),
            "type": request.form.get("type"),
            "created_by": username
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, update_recipe)
        flash("Recipe Updated!")

    users_cookbook = mongo.db.recipes.find({"created_by": username})
    user_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    return render_template("edit-recipe.html", username=username,
                           recipe=user_recipe,
                           users_cookbook=users_cookbook)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
