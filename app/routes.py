from flask import Blueprint
import requests
from flask import Flask, jsonify, abort, make_response, request
# from genres_predictor import GenrePredictor
import json
# import db_utility
import argparse
import os
from app import config
from app.gateway import updateMultilayerResult, updateGenreResult

bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    return "Hello, Flask with Docker and Gunicorn!"


@bp.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@bp.route('/gramusik/v1/predictmultilayer/<string:youtube_id>', methods=['GET'])
def predict_multilayer(youtube_id):
    req = config.flask_host_port + config.flask_app_context + youtube_id
    print(req)
    r = requests.get(req)
    respobj = json.loads(r.text)
    style1 = respobj['combinedprediction_withlable'][0][0]
    resultlist = []

    resultlist.append(respobj)

    while style1 in config.style_port:
        print(style1)
        style1Req = config.style_port[style1] + config.flask_app_context + youtube_id
        print(style1Req)
        try:
            style1Resp = requests.get(style1Req)
            style1RespObj = json.loads(style1Resp.text)
            resultlist.append(style1RespObj)

            style1 = style1RespObj['combinedprediction_withlable'][0][0]
        except Exception as e:
            print(e)
            break

    combinedresult = updateMultilayerResult(resultlist, 3)

    # return jsonify(resultlist)
    return jsonify(combinedresult)


@bp.route('/gramusik/v1/predictcombined/<string:youtube_id>', methods=['GET'])
def predict_combined(youtube_id):
    req = config.flask_host_port + config.flask_app_context + youtube_id
    print(req)
    r = requests.get(req)
    respobj = json.loads(r.text)
    style1 = respobj['combinedprediction_withlable'][0][0]
    style2 = respobj['combinedprediction_withlable'][1][0]
    print(style1)
    print(style2)
    if style1 in config.style_port:
        style1Req = config.style_port[style1] + config.flask_app_context + youtube_id
        print(style1Req)
        style1Resp = requests.get(style1Req)
        style1RespObj = json.loads(style1Resp.text)

    if style2 in config.style_port:
        style2Req = config.style_port[style2] + config.flask_app_context + youtube_id
        print(style2Req)
        style2Resp = requests.get(style2Req)
        style2RespObj = json.loads(style2Resp.text)

    combinedresult = updateGenreResult(respobj, style1RespObj, style2RespObj, 4, 3)

    return jsonify(combinedresult)
