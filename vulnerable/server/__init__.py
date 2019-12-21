#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask, Blueprint, render_template, request
from urllib.parse import unquote_plus
import MySQLdb
import random
import json
import sys
import os

from .database import *


def create_app(db_size=250):
    reinit_database(total_users=db_size)
    app = Flask(__name__)
    from .vuln.routes import vulns
    app.register_blueprint(vulns)
    return app
