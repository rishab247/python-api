from flask import Flask, jsonify, request, make_response, logging
import jwt
import json
import datetime
import database as db
from functools import wraps

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({'msg': 'Fuck Off', }), 401


@app.route("/Askme", methods=['POST'])
def Askme():
    try:
        jsondata = request.get_data().decode("utf-8")
        jsondata = json.loads(jsondata)
    except Exeption  as e:
        print(str(e))

    return jsonify({'msg': 'Fuck Off! Again', }), 401

