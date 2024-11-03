from flask import Blueprint, render_template, request, flash,redirect, session
from .models import Doc,Patient, P_details
from  . import db
from werkzeug.security import generate_password_hash, check_password_hash
import time
from flask_login import login_user, login_required, logout_user, current_user

auth= Blueprint('auth',__name__)

phno=""

@auth.route("/ptlogin", methods=["GET","POST"])
def patient_login():
    if request.method == "POST":
        phno = request.form.get("phno")
        password = request.form.get("password")
        user = Patient.query.filter_by(phone_no=phno).first()
        if user:
            if check_password_hash(user.password, password):
                session['message'] = {'type': 'success', 'text': 'Logged in successfully!'}
                login_user(user, remember=True)
                phno= Patient.query.filter_by(phone_no=phno)
                return redirect("/user")
            else:
                session['message'] = {'type': 'error', 'text': 'Incorrect password'}
        else:
            session['message'] = {'type': 'error', 'text': 'Phone number does not exist'}
    return render_template("patient_login.html")



@auth.route("/dclogin", methods=["GET","POST"])
def doctor_login():
    return render_template("doctor_login.html")




@auth.route("/dcsignup",  methods=["GET","POST"])
def doctor_signup():
    pass




@auth.route("/ptsignup", methods=["GET","POST"])
def patient_signup():
    if request.method=="POST":
        phno=request.form.get("phno")
        name= request.form.get("name")
        password1=request.form.get("password1")
        password2=request.form.get("password2")
        user = Patient.query.filter_by(phone_no=phno).first()
        if user:
            session['message'] = {'type': 'error', 'text': 'Phone number already exists'}

        elif password1!=password2:
            session['message'] = {'type': 'error', 'text': 'Passwords do not match'}

        elif len(phno)<10:
            session['message'] = {'type': 'error', 'text': 'Invalid Phone number'}
        elif len(name)<4:
            session['message'] = {'type': 'error', 'text': 'Invalid Name'}

        else:
            new_usr= Patient(name=name, password=generate_password_hash(password1), phone_no=phno)
            db.session.add(new_usr)
            db.session.commit()
            session['message'] = {'type': 'success', 'text': 'Account Created'}
            login_user(new_usr, remember=True)
            return redirect("/user")

    return  render_template("ptsignup.html")

@auth.route("/user", methods=["GET", "POST"])
@login_required
def user_view():
    if request.method == "POST":
        fname=request.form.get("fname")
        email=request.form.get("email")
        age=request.form.get("age")
        gender=request.form.get("gender")
        bld_grp=request.form.get("blood_group")
        existing=request.form.get("existing")
        allergies = request.form.get("allergies")
        height = "xxx"

        print("Deetail:")
        print(fname)
        print(email)
        print(age)
        print(gender)
        print(bld_grp)
        print(existing)

        if P_details.first:
            new_usr=P_details(fname=fname, email=email, age=age, gender=gender,
                          bld_grp=bld_grp, existing=existing,  allergies=allergies, 
                          first=False, height=height)
        
            db.session.add(new_usr)
            db.session.commit()
            return redirect("/user/dashboard")

    return render_template("user.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    session['message']={'type': 'success', 'text': 'Successfully Logged Out'}
    return redirect("/")

