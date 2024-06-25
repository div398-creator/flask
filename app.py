# from flask import Flask, redirect, url_for,  render_template
from flask import *
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "HELLO! This is the main page <h1> HELLO WELCOME <H1>"

  
@app.route('/html')
def hello_html():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
    
