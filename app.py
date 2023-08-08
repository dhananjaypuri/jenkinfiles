from flask import Flask, redirect, render_template

app = Flask(__name__);

@app.route('/')
def home():
    return "<h1>This is the home page</h1>";

@app.route('/contact')
def contact():
    return "<h1>This is the Contact page</h1>";

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0');