#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from server import create_app
import argparse


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-s", "--size", metavar="db_size", type=int, default=250, help="specify total rows to use in the database", required=False)
    args = p.parse_args()
    app = create_app(db_size=args.size)
    app.run(debug=False, host="127.0.0.1", port=80)


if __name__ == "__main__":
    main()
