#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from . import *


class Samples(object):

    _FILE_DIR = "/".join(__file__.split("/")[:-1] + ["wordlists"])
    _FIRST_NAMES = "/".join((_FILE_DIR, "first_names.txt"))
    _LAST_NAMES = "/".join((_FILE_DIR, "last_names.txt"))
    _PASSWORDS = "/".join((_FILE_DIR, "passwords.txt"))

    def __init__(self, sample_size=250):
        self.sample_size = sample_size

    def __repr__(self):
        return repr("\n".join(self.rows))

    def __str__(self):
        return "\n".join(self.rows)

    def __len__(self):
        return len(self.rows)

    def __iter__(self):
        for _ in self.yield_rows:
            yield _

    def __getitem__(self, index):
        for i, _ in enumerate(self.rows):
            if index == i:
                return _

    @property
    def rows(self):
        return list(self.yield_rows)

    @property
    def yield_rows(self):
        zip_data = (self.first_names, self.last_names, self.passwords)
        for i, n in enumerate(zip(*zip_data)):
            fs_row = "(%d, %s, %s, %s)"
            row = ((i+1), repr(n[0]), repr(n[1]), repr(n[2]))
            yield fs_row % row

    @property
    def first_names(self):
        _names = self._first_name_data.split("\n")
        names = [_.title() for _ in _names]
        random.shuffle(names)
        return names[:self.sample_size]

    @property
    def last_names(self):
        _names = self._last_name_data.split("\n")
        names = [_.title() for _ in _names]
        random.shuffle(names)
        return names[:self.sample_size]

    @property
    def passwords(self):
        names = self._password_data.split("\n")
        random.shuffle(names)
        return names[:self.sample_size]

    @property
    def _first_name_data(self):
        return Samples._load_file(self._FIRST_NAMES)

    @property
    def _last_name_data(self):
        return Samples._load_file(self._LAST_NAMES)

    @property
    def _password_data(self):
        return Samples._load_file(self._PASSWORDS)

    @staticmethod
    def _load_file(filename):
        with open(filename) as f:
            return f.read().strip()
