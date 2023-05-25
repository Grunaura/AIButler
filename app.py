"""
Author: Adam Messick
Date: 5/24/2023

This is the main entry point for our web application. It sets up a Flask server and routes.
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    # Placeholder for processing information
    # This is where you would call your functions to process the input data
    # data = request.form
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)
