from app import app
from flask import Flask, redirect, url_for, request, render_template
import json
import time
from datetime import datetime
import subprocess
import random

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

#from app import db
#from app.models import Entry

#Main Page
@app.route('/')
@app.route('/index')
def index():
    score, magnitude = defineGoogleClient()
    return render_template("index.html", variable=score, variable2=magnitude)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/members")
def members():
    return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return name


def defineGoogleClient():
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    # this can be read from file later
    text = u'Hello, world!'
    document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    return sentiment.score, sentiment.magnitude;
    # print('Text: {}'.format(text))
    # print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
