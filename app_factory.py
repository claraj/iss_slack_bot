from flask import Flask

def factory():
    app = Flask(__name__)
    return app
