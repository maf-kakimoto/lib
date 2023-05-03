# -*- coding: utf-8 -*-

from lib import config
from lib import load_yaml

local_path = ''


def _xxx():

    path = load_yaml._load_yaml(local_path + 'path.yml')
    config.xxx = path['xxx']
