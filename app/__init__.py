#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## Epytodo
## File description:
##
##

from flask import current_app as app
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

def get_application():
    return app
