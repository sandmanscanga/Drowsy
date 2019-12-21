#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from . import *

vulns = Blueprint("vulns", __name__)


@vulns.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@vulns.route("/search-get", methods=["GET"])
def search_get():
    if request.method == "GET" and request.query_string:
        raw_query = request.query_string.decode()
        query_dict = {}
        for fields in raw_query.split("&"):
            field = fields.split("=")
            query_dict[field[0]] = field[1] if len(field) <= 2 else "=".join(field[1:])
        if "last_name" in query_dict:
            query = unquote_plus(query_dict["last_name"])
            if query:
                try:
                    result = search_database(query)
                except:
                    pass
                else:
                    if result:
                        return render_template("search_get.html", result=result)
    return render_template("search_get.html")


@vulns.route("/search-get-blind", methods=["GET"])
def search_get_blind():
    if request.method == "GET" and request.query_string:
        raw_query = request.query_string.decode()
        query_dict = {}
        for fields in raw_query.split("&"):
            field = fields.split("=")
            query_dict[field[0]] = field[1] if len(field) <= 2 else "=".join(field[1:])
        if "id" in query_dict:
            query = unquote_plus(query_dict["id"])
            if query:
                try:
                    result = search_database(query, by_name=False)
                except:
                    pass
    return render_template("search_get_blind.html")


@vulns.route("/search-post", methods=["GET", "POST"])
def search_post():
    if request.method == "POST":
        query = request.form.get("id")
        if query:
            try:
                result = search_database(query, by_name=False)
            except:
                pass
            else:
                if result:
                    return render_template("search_post.html", result=result)
    return render_template("search_post.html")


@vulns.route("/search-post-blind", methods=["GET", "POST"])
def search_post_blind():
    if request.method == "POST":
        query = request.form.get("last_name")
        if query:
            try:
                result = search_database(query)
            except:
                pass
    return render_template("search_post_blind.html")
