# -*- coding:utf-8 -*-

from lib import load_text


def _headers():

    file = ''
    user_agent = load_text._load_as_text(file)
    headers = {'User-Agent': user_agent}

    return headers
