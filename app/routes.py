from flask import flash, redirect, render_template, url_for

from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Michael"}
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Susan"}, "body": "The Avengers movie was so cool!"},
        {"author": {"username": "Mint"}, "body": "Akiba, I'll fight for you!"},
        {"author": {"username": "Pheobe"}, "body": "For all otaku!"},
        {"author": {"username": "Victoria"}, "body": "Still one of you!"},
        {"author": {"username": "densetsu.exe"}, "body": "BURNING ON!"},
    ]
    return render_template("index.html", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            "Login requested for user {}, remember_me={}".format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)
