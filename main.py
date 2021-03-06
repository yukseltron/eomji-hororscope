# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import emoji
import sys
import importlib
try:
    from google.appengine.api import urlfetch
    from requests_toolbelt.adapters import appengine
    appengine.monkeypatch()
except ImportError:
    pass

if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")
    
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def result():
    sign = request.form['sign']
    emojiPrediction = emoji.analyzeScope(sign)
    return render_template("result.html", horoscope = emojiPrediction)


if __name__=='__main__':
    app.run(debug=True)
