import os
import pathlib
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<club_name>")
def club_results_home(club_name):
    return render_template("club_results_home.html", club_name=club_name)

@app.route('/<club_name>/upload-results', methods=['POST'])
def upload_results(club_name):
    if request.method == 'POST':
        file = request.files['resultsFile']
        if file:
            filename = "results.htm"
            pathlib.Path("static/" + club_name).mkdir(parents=True, exist_ok=True)
            file.save(os.path.join("static", club_name , filename))
            resp = jsonify(success=True)
            return resp

@app.route('/<club_name>/upload-splits', methods=['POST'])
def upload_splits(club_name):
    if request.method == 'POST':
        file = request.files['splitsFile']
        if file:
            filename = "splits.htm"
            pathlib.Path("static/" + club_name).mkdir(parents=True, exist_ok=True)
            file.save(os.path.join("static", club_name , filename))
            resp = jsonify(success=True)
            return resp
