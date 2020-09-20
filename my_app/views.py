from my_app import app
from flask import render_template, request, redirect, url_for, flash
import requests

app.secret_key = '3'

@app.route("/", methods=['GET','POST'])
def home():
    if request.method == "POST":
        if request.form["login"] == "teacher":
            return redirect(url_for("teacher"))
        if request.form["login"] == "student":
            return redirect(url_for("student"))
    return render_template("/home/landing.html")

@app.route("/teacher")
def teacher():
    return render_template("/teacher/dashboard.html")

@app.route("/student")
def student():
    return render_template("/student/dashboard.html")