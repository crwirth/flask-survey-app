from flask import Flask, request, render_template, redirect, flash, jsonify
from surveys import satisfaction_survey as survey
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def home_page():
    return render_template("/home.html", survey=survey)

@app.route('/start', methods=["POST"])
def start_survey():
    return redirect("/questions/0")