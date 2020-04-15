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
import pymysql as sql
from config import *

connect = sql.connect(host=DATABASE_HOST,
                        db=DATABASE_NAME,
                        user=DATABASE_USER,
                        password=DATABASE_PASS,
                        unix_socket=DATABASE_SOCK)
cursor = connect.cursor()

student = None
todo = None

def create_user(data):
    empty = cursor.execute("SELECT * FROM user WHERE username='{}' AND password='{}';".format(data.get('username'),
                                                                                                data.get('password')))
    if empty > 0:
        return jsonify(error="Sorry. This account exist already")
    else:
        cursor.execute("INSERT INTO user (username, password) VALUES ('{}', '{}');".format(data.get('username'),
                                                                                            data.get('password')))
        return jsonify(result="Sucess. Your account has been created")