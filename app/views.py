#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## Epytodo
## File description:
##
##

from flask import render_template
from app import app

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def route_home():
    return "Hello world !\n"

@app.route('/user/<username>', methods=['POST'])
def route_add_user(username):
    return "User added !\n"

def route_index():
    return render_template("index.html",
                           title is "Hello World",
                           myContent is "My SUPER content !!")
@app.route ('/user/<username>', methods=['GET'])
def route_user(username):
    return render_template("index.html",
                           title="Hello"+username,
                           myContent="My SUPER content for"+username+"!!!")
