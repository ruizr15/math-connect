from my_app import app
from flask import render_template, request, redirect
import requests

@app.route("/")
def home():
    return render_template("/home/landing.html")

@app.route("/teacher")
def teacher():
    return render_template("/teacher/dashboard.html")

@app.route("/student")
def student():
    return render_template("/student/dashboard.html")