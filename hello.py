"""Tiny Flask Example

From https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart

Requires you to install flask in your virtual environment:

  $ . .venv/bin/activate
  OR
  > .venv\Scripts\activate

  $ pip install flask

To run this on windows:

  Activate your environment if you haven't already.

  PS C:\path\to\app> $env:FLASK_ENV = "development"
  PS C:\path\to\app> $env:FLASK_APP = "tiny.py"
  PS C:\path\to\app> flask run

To run this on linux:

  $ export FLASK_ENV=development
  $ FLASK_APP=tiny.py flask run

Then in a browser go to http://127.0.0.1:5000/
"""
from flask import Flask


app = Flask(__name__)

def add(x, y):
    return x + y 
    

# @app.route() lets you set the url path that will trigger each view.
# '/' is the root of the domain. If your website was hosted at example.com
# then the full url would be https://example.com/
# If the path was '/do/thing/' then the full url would be https://example.com/do/thing/
@app.route('/')
def hello_world(num):
      return "Hello, world!"
             

    
def test_add():
      assert add(7, 1) == 8
      
    

  
  