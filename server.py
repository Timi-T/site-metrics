#!/usr/bin/python3
"""
Create a flask app to get metrics
"""

import json
from flask import Flask, make_response, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/', methods=['GET'], strict_slashes=False)
def landing():
    """Landing page for API"""
    return ({'Instruction': 'Use (/metrics) endpoint to get metric for all your sites'})

@app.route('/metrics', methods=['GET'], strict_slashes=False)
def metrics():
    """Metris Payload"""
    with open("logs") as f:
        logs = json.load(f)
    return(logs)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)