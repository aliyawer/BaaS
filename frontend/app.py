#!flask/bin/python
from flask import Flask, jsonify
import subprocess
import sys

app = Flask(__name__)


@app.route('/baas', methods=['GET'])
def baas_project():
    return "Running BaaS project!!!!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
