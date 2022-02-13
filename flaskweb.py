# KVCC 
# CIS-226-23199
# Advanced Python Programming

'''
Design: How will you solve the problem?
I will solve this problem by using "flask" because is a web framework that could create web applications in python easier.
Develop:
First, create a GIT repository, and then in the local folder create a virtual environment, 
and then install the flask package. Then add to those features included with the library. 
I used an HTML template to print the contents of the website. The template is returned to the function index of the web page.
Test:
The idea is to test asserting a simple calculation using a virtual environment running pytest from the terminal. 
I'm still not able to run the test. I don't know if my error is in the "hello.py" file or the test file.
How to use the program:
On the terminal: First activate the virtual environment '. venv/bin/activate', Second export the file 'export FLASK_APP=hello.py' run the framework 'flask run'. 
The website is running on http://127.0.0.1:5000/

The development time for this assignment is 6hrs
'''

from flask import Flask, render_template

app = Flask(__name__)

def add(x, y):
    return x + y

@app.route('/')
def index():
    # Render a template instead of returning a string
    return render_template('main.html')

    
    


             

    

      
    

  
