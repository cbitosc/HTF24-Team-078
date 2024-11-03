from flask import Blueprint, Flask, render_template
import os
from groq import Groq
from .models import P_details, Patient
from dotenv import load_dotenv
from flask_login import login_user, login_required

views=Blueprint('views',__name__)

load_dotenv()
key=os.getenv('GROQ_API_KEY')
client = Groq(api_key=key)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/about')
def info():
    return render_template("about.html")

@views.route("/contact")
def contact():
    return render_template("contact_us.html")

@views.route("/user/dashboard")
@login_required
def dashboard():
    name=str(P_details.fname)
    return render_template("base2.html", patient_name=name)

@views.route("/user/dashboard/chat")
@login_required
def chat():
    entry=P_details.query.order_by(P_details.id.desc()).first()
    print(entry)
    # final=summary(str(entry.fname), str(entry.gender), str(entry.bld_grp), str(entry.existing), str(entry.allergies))
    return render_template("chat.html")

@views.route("/user/dashboard/logger")
@login_required
def logger():
    return render_template("logger.html")

@views.route("/user/dashboard/track")
@login_required
def track():
    return render_template("track.html")
    
def summary(name,gend,bld_gr,dis,aller):
    completion = client.chat.completions.create(
        model="llama3-groq-70b-8192-tool-use-preview",
        messages=[
            {
                "role":"system",
                "content":("You are a doctor giving a long health summary of a person, given his blood group, any diseases, any allergies, and their gender.")
            },
            {
                "role": "user",
                "content": ("My name is "+name+" where my gender is "+gend+", my blood group is "+bld_gr+"-, I have "+dis+" diseases and "+aller+" allergies.")
            }
        ],
        temperature=0.5,
        max_tokens=1024,
        top_p=0.65,
        stream=True,
        stop=None,
    )
    final=""
    for chunk in completion:
        final+=(chunk.choices[0].delta.content or "")

    return final
