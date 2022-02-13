# KVCC 
# CIS-226-23199
# Advanced Python Programming

'''
Design: How will you solve the problem?
I will solve this problem by using "flask" because is a web framework that could create web applications in python easier.
Develop:
First create a GIT repository, and then in the local folder create a virtual enviroment, 
and then installing the flask package . Then add to that features included with the library. 
I used a HTML template to print the contents of the web site. The template is returned into the function index of the web page.
Test:
The idea is to test asserting a simple calculation using a virtual environment running pytest from the terminal. I still not able to run test.
How to use the program:

The development time for this assignment is 8hrs
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Render a template instead of returning a string
    return render_template('main.html')


             

    

      
    

  
