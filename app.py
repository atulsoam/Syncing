from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    sum = 1+2
    return f"Hello from flaskdkvv {sum}"