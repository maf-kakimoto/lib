# -*- coding:utf-8 -*-

def _load_as_text(file):

    with open(file) as textfile:
        dataTEXT = textfile.read()
        dataTEXT = dataTEXT[:-1]  # delete last '\n'

    return dataTEXT
