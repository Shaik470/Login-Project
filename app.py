from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the App! Go to /login or /payment"

if __name__ == '__main__':
    app.run(debug=True, port=5000)