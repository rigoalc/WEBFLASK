# KVCC 
# CIS-226-23199
# Advanced Python Programming
# 02/13/2022

'''
Design: How will you solve the problem?
I will solve this problem by using "flask" because is a web framework that could create web applications in python easier.
Develop:
First, create a GIT repository, and then in the local folder create a virtual environment, 
and then install the flask package. Then add to those features included with the library. 
I used an HTML template to print the contents of the website. The template is returned to the function index of the web page.
Test:
The idea is to test asserting a simple calculation using a virtual environment running pytest from the terminal. 
How to use the program:
On the terminal: First activate the virtual environment '. venv/bin/activate', Second export the file 'export FLASK_APP=hello.py' run the framework 'flask run'. 
The website is running on http://127.0.0.1:5000/

The development time for this assignment is 6hrs
'''

from flask import Flask, render_template #Import library flask and template


def add(x, y):
    return x + y

app = Flask(__name__)



@app.route('/')
def index():
    #Main Page
    return render_template('main.html')#return html from file main