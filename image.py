# -*- coding: utf-8 -*-

from PIL import Image


def show(file):

    im = Image.open(file)
    im.show()
