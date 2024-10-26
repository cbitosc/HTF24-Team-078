from flask import Blueprint, Flask, render_template

views=Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/about')
def info():
    return render_template("about.html")

@views.route("/contact")
def contact():
    return render_template("contact_us.html")

@views.route("/user")
def user_view():
    pass
