# KVCC 
# CIS-226-23199
# Advanced Python Programming

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Render a template instead of returning a string
    return render_template('main.html')


             

    

      
    

  
