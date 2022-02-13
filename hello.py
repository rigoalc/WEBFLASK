#
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Render a template instead of returning a string
    return render_template('main.html')

def test_add():
      assert add (7,1) == 8

             

    

      
    

  
  