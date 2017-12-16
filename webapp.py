from flask import Flask, request, Markup, render_template, flash
import json
import os

app = Flask(__name__)

def get_title_options():
    with open('classics.json') as classics_data:
        classics = json.load(classics_data)
    titles = []
    for t in classics:
        if t["bibliography"]["title"] not in titles:
            if len(t["bibliography"]["title"]) < 80:
                titles.append(t["bibliography"]["title"])
            else:
                titles.append(t["bibliography"]["title"][:80] + "...")
    options = ""
    for o in titles:
        options += Markup("<option value=\"" + o + "\">" + o + "</option>")
    return options

def get_title_data(title, info):
    with open('classics.json') as classics_data:
        classics = json.load(classics_data)
    i = str(info) + ":"
    b = " "
    d = " "
    for n in classics:
        if n["bibliography"]["title"] == title:
            if info == "Reading Difficulty Information":
                b = "<h4> Flesch Reading Ease: " + str(n["metrics"]["difficulty"]["flesch reading ease"]) + "<br> Automated Readability Index: " + str(n["metrics"]["difficulty"]["automated readability index"]) + "<br> Coleman Liau Index: " + str(n["metrics"]["difficulty"]["coleman liau index"]) + "<br> Gunning Fog: " + str(n["metrics"]["difficulty"]["gunning fog"]) + "<br> Linsear Write Formula: " + str(n["metrics"]["difficulty"]["linsear write formula"]) + "<br> Dale Chall Readability Score: " + str(n["metrics"]["difficulty"]["dale chall readability score"]) + "<br> Flesch Kincaid Grade: " + str(n["metrics"]["difficulty"]["flesch kincaid grade"]) + "<br> Smog Index: " + str(n["metrics"]["difficulty"]["smog index"]) + "<br> Difficult Words: " + str(n["metrics"]["difficulty"]["difficult words"]) + "</h4>"
            if info == "Statistics Information":
                b = "<h4> Polysyllables: " + str(n["metrics"]["statistics"]["polysyllables"]) + "<br> Characters: " + str(n["metrics"]["statistics"]["characters"]) + "<br> Average Sentence Length: " + str(n["metrics"]["statistics"]["average sentence length"]) + "<br> Words: " + str(n["metrics"]["statistics"]["words"]) + "<br> Sentences: " + str(n["metrics"]["statistics"]["sentences"]) + "<br> Syllables: " + str(n["metrics"]["statistics"]["syllables"]) + "<br> Average Sentence per Word: " + str(n["metrics"]["statistics"]["average sentence per word"]) + "<br> Average Letter per Word: " + str(n["metrics"]["statistics"]["average letter per word"]) + "</h4>"
            if info == "Sentiments Information":
                b = "<h4> Polarity: " + str(n["metrics"]["sentiments"]["polarity"]) + "<br> Subjectivity: " + str(n["metrics"]["sentiments"]["subjectivity"]) + "</h4>"
            if info == "Publication Information":
                b = "<h4> Date of Publication: " + str(n["bibliography"]["publication"]["month name"]) + " " + str(n["bibliography"]["publication"]["day"]) + ", " + str(n["bibliography"]["publication"]["year"]) + "</h4"
            if info == "Author Information":
                b = "<h4> Name: " + str(n["bibliography"]["author"]["name"]) + "<br> Birth: " + str(n["bibliography"]["author"]["birth"]) + "<br> Death: " + str(n["bibliography"]["author"]["death"]) + "</h4>"
            if info == "Subjects Information":
                b = "<h4> Subjects: " + str(n["bibliography"]["subjects"]) + "</h4>"
            if info == "Congress Classification Information":
                b = "<h4> Congress Classifications: " + str(n["bibliography"]["congress classifications"]) + "</h4>"
    d = Markup("<h3>" + title + " " + i + "</h3>" + b)
    return d

# def get_genre_data(genre):
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

@app.route("/bygenre")
def render_t2():
#         if 'class' in request.args:
#         return render_template('tab2.html', data = get_genre_data(request.args['genre']))
#     else:
        return render_template('tab2.html')

@app.route("/bylevel")
def render_t3():
        return render_template('tab3.html')

if __name__=="__main__":
    app.run(debug=False)

    
