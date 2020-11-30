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
        "You're not as alone as you feel",
        "It's hard to see solutions when in distress",
        "Situations can change, emotions aren't permanent",
        "Your mistakes don't define you",
        "Do what you can today, it's worth it",
        "You are important to me",
        "You're doing your best and that isn't easy",
        "I know it's hard to keep going, but please don't go away",
        "I believe in you, even if you don't",
        "Sometimes it’s okay if the best thing you did all day was get out of bed",
        "Life is messy, chaotic, confusing and that’s okay",
        "You are not the mistakes you’ve made",
        "Sometimes you just need to cry. It’s okay to have emotions",
        "Be nice to yourself, you’re doing your best",
        "You are special. Never stop being proud of who you are",
        "The tears you are currently shedding will not last forever. Better days are coming, just hang on a little",
        "No matter how dark this day is, it will undoubtedly give way to a sunnier tomorrow. Just believe in yourself and hold on for a little while",
        "Celebrate your life, come what may, for you are strong and beautiful",

    ]
    new_reason = random.choice(reasons)
    while(new_reason == curr_reason):
        new_reason = random.choice(reasons)
    return jsonify(new_reason)