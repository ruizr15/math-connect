from my_app import app
from flask import render_template, request, redirect
import requests

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("/teacher/dashboard.html")
