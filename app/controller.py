#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## Epytodo
## File description:
##
##


from app import app
from flask import render_template
from flask import jsonify
from flask import Flask,request
import pymysql as sql
import json

def json_checker(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

def transform_request_to_user(json_data, form_data):
    if type(json_data) is dict:
        data = json_data
    else:
        data = {"username": form_data['username'], "password": form_data['password']}
    return data

def transform_request_to_task(json_data, form_data):
    if type(json_data) is dict:
        data = json_data
    else:
        data = {"title":form_data['title'], "begin":form_data['begin'], "end":form_data['end'], "status":form_data['status']}
    return data