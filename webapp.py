from flask import Flask, request, Markup, render_template, flash, Markup
import json
import os

app = Flask(__name__)

@app.route("/")
def render_main():
        return render_template('home.html')

if __name__=="__main__":
    app.run(debug=False)

    
