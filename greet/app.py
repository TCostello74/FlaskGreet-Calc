from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    """Will simply print welcome"""
    return "welcome"

@app.route('/welcome/home')
def say_welcome_home():
    """Will simply print welcome home"""
    return "welcome home"

@app.route('/welcome/back')
def say_welcome_back():
    """Will simply print welcome back"""
    return "welcome back"