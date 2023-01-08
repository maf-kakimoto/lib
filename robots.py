# -*- coding: utf-8 -*-

import urllib.robotparser


def _robots(url):

    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(url)
    rp.read()

    return rp
