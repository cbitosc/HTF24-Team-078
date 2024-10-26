from flask import Blueprint, render_template, request, flash,redirect
from .models import Doc,Patient
from  . import db
from werkzeug.security import generate_password_hash, check_password_hash


auth= Blueprint('auth',__name__)

@auth.route("/ptlogin", methods=["GET","POST"])
def patient_login():
    if request.method == "POST":
        phno=request.form.get("phno")
        password=request.form.get("password")

        user = Patient.query.filter_by(phone_no=phno).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged In Successfully!", category="success")
            else:
                flash("Incorrect password", category="error")
        else:
            flash("Phone Number does not exist", category="error")

    return render_template("patient_login.html")

@auth.route("/dclogin", methods=["GET","POST"])
def doctor_login():
    return render_template("doctor_login.html")

@auth.route("/dcsignup",  methods=["GET","POST"])
def doctor_signup():
    print(request.form)
    if request.method=="POST":
        phno=request.form.get("phno")
        name= request.form.get("name")
        password1=request.form.get("password1")
        password2=request.form.get("password2")

        user = Patient.query.filter_by(phone_no=phno).first()
        if user:
            flash("Phone number already in use",  category="error")
            return redirect("/user")
        elif(password1!=password2):
            flash("Passwords dont match", category="error")
        elif len(phno)<10:
            flash("Invalid Phone Number", category="error")
        elif len(name)<4:
            flash("Name should be at least 4 characters long", category="error")
        else:
            print(name) 
            print(password1) 
            print(phno) 
            new_usr=Doc(name=name, password=generate_password_hash(password1), phone_no=phno)

            db.session.add(new_usr)
            db.session.commit()
            flash("Doctor account created successfully", category="success")
            return redirect("/")

    return  render_template("dcsignup.html")

@auth.route("/ptsignup", methods=["GET","POST"])
def patient_signup():
    if request.method=="POST":
        phno=request.form.get("phno")
        name= request.form.get("name")
        password1=request.form.get("password1")
        password2=request.form.get("password2")

        if(password1!=password2):
            flash("Passwords dont match", category="error")
        if len(phno)<10:
            flash("Invalid Phone Number", category="error")
        if len(name)<4:
            flash("Name should be at least 4 characters long", category="error")
        else:
            new_usr= Patient(name=name, password=generate_password_hash(password1), phone_no=phno)
            db.session.add(new_usr)
            db.session.commit()

            flash("Patient account created successfully", category="success")



    return  render_template("ptsignup.html")

