#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## Epytodo
## File description:
##
##

from flask import render_template
from flask import jsonify
from flask import Flask,request
from app import app
from app import controller
from app import models
import pymysql as sql


@app.route('/', methods=['GET'])
def route_index():
    return render_template("index.html",
                            title="Hello World",
                            myContent="My SUPER content !!")

@app.route('/index', methods=['GET'])
def route_home():
    return "Hello world !\n"

@app.route('/user/<username>', methods=['POST'])
def route_add_user(username):
    return "User added !\n"

@app.route ('/user/<username>', methods=['GET'])
def route_user(username):
    return render_template("index.html",
                            title="Hello"+username,
                            myContent="My SUPER content for"+username+"!!!")

@app.route('/register', methods=['POST'])
def route_register():
    try:
        data = controller.transform_request_to_user(json_data=request.json, form_data=request.form)
        return models.create_user(data)
    except:
        return jsonify(error="internal error")