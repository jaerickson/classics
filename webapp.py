from flask import Flask, request, Markup, render_template, flash
import json
import os

app = Flask(__name__)

def get_title_options():
    with open('classics.json') as classics_data:
        classics = json.load(classics_data)
    titles = []
    for t in classics:
        if t["bibliography"]["title"] not in titles and len(t["bibliography"]["title"]) < 80:
            titles.append(t["bibliography"]["title"])
        if t["bibliography"]["title"] not in titles and len(t["bibliography"]["title"]) > 80:
            titles.append(t["bibliography"]["title"][:80] + "...")
    options = ""
    for o in titles:
        options += Markup("<option value=\"" + o + "\">" + o + "</option>")
    return options

def get_title_data(title, info):
    with open('classics.json') as classics_data:
        classics = json.load(classics_data)
    b = " "
    i = " "
    d = " "
    for n in classics:
        if n["bibliography"]["title"] == title:
            if info == "difficulty" or info == "statistics" or info == "sentiments":
                b = str(n["metrics"][info] + "h")
                if info == "difficulty":
                    i = "Reading Difficulty Information:"
                if info == "statistics":
                    i = "Statistics Information:"
                if info == "sentiments":
                    i = "Sentiments Information:"
            if info == "publication" or info == "author" or info == "subjects" or info == "congress classifications":
                b = str(n["bibliography"][info])
                if info == "publication":
                    i = "Publication Information:"
                if info == "author":
                    i = "Author Information:"
                if info == "subjects":
                    i = "Subjects Information:"
                if info == "congress classifications":
                    i = "Congress Classification Information:"
    d = Markup("<h3>" + title + " " + i + "</h3>" + "<h4>" + b + "</h4>")
    return d

# def get_class_data(class):
#     with open('classics.json') as classics_data:
#         classics = json.load(classics_data)



@app.route("/")
def render_main():
        return render_template('home.html')

@app.route("/bytitle")
def render_t1():
    if 'title' in request.args:
        return render_template('tab1.html', options = get_title_options(), data = get_title_data(request.args['title'], request.args['info']))
    else:
        return render_template('tab1.html', options = get_title_options())

@app.route("/byclass")
def render_t2():
#         if 'class' in request.args:
#         return render_template('tab2.html', data = get_class_data(request.args['class']))
#     else:
        return render_template('tab2.html')

@app.route("/bylevel")
def render_t3():
        return render_template('tab3.html')

if __name__=="__main__":
    app.run(debug=False)

    
