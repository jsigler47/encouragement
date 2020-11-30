from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/_get_reason')
def get_reason():
    curr_reason = request.args.get('reason')
    reasons = [
        "You're not as alone as you feel.",
        "It's hard to see solutions when in distress",
        "Situations can change, emotions aren't permanent",
        "Your mistakes don't define you.",
        "Do what you can today, it's worth it.",
        "You are important to me.",
        "You're doing your best and that isn't easy.",
        "I know it's hard to keep going, but please don't go away.",
        "I believe in you, even if you don't."
    ]
    new_reason = random.choice(reasons)
    while(new_reason == curr_reason):
        new_reason = random.choice(reasons)
    return jsonify(new_reason)