from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import json
import scrapers.devpost as devpost
import scrapers.hackerearth as hackerearth
import scrapers.mlh as mlh

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hacks', methods=['GET'])
def getMLHHacks():
    hackathons = []
    hackathons = devpost.devpost(hackathons)
    hackathons = mlh.mlh(hackathons)
    hackathons = hackerearth.hackerearth(hackathons)
    return jsonify(data=hackathons)


if __name__ == "__main__":
    app.run()
