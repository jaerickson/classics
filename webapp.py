from flask import Flask, request, Markup, render_template, flash, Markup
import json
import os

app = Flask(__name__)

@app.route("/")
def render_main():
        return render_template('home.html')

@app.route("/bytitle")
def render_t1():
        return render_template('tab1.html')

@app.route("/bygenre")
def render_t2():
        return render_template('tab2.html')

@app.route("/bylevel")
def render_t3():
        return render_template('tab3.html')

if __name__=="__main__":
    app.run(debug=False)

    
