import random
from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/docs')
def docs():
    return render_template('docs.html')

@app.route('/api/quote')
def quote():
    quote_list = []
    with open('quotes.txt') as quotes:
        quote_list = quotes.readlines()

    return jsonify({"quote": random.choice(quote_list)})
