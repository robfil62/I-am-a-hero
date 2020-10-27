from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"asso":{"qui":"Ici des infos sur l'asso", "pourquoi":"Ici pourquoi les aider"}})