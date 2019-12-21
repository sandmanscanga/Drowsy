#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from . import *


def load_creds(filename=None):
    if not filename:
        filename = "/".join(__file__.split("/")[:-1] + ["creds.json"])
    with open(filename) as f:
        return json.load(f)


_CREDS = load_creds()
