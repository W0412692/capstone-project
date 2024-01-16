#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
allowed_methods = ["GET"]


@app.route("/api", methods=allowed_methods)
def hello_world():
    return {"a": "B"}

@app.route("/asdasdasd", methods=allowed_methods)
def xswdvfrgbyhjukil():
    return "woah, what an efficient way of setting up a backend"