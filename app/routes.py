from app import app
from flask import Flask, redirect, url_for, request, render_template
import json
import time
from datetime import datetime
import subprocess
import random

#from app import db
#from app.models import Entry

#Main Page
@app.route('/')
@app.route('/index')
def index():
    return "Index!"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/members")
def members():
    return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return name

