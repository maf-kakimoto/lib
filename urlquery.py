# -*- coding: utf-8 -*-

def _multiparams(base, params):

    i = 0
    url = base
    for key in params:

        if i == 0:
            url += '?'
        else:
            url += '&'
        url += key + '=' + params[key]
        i += 1

    return url
