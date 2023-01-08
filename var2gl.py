# -*- coding:utf-8 -*-

from lib import config
from lib import load_yaml

local_path = ''


def _bet():

    path = load_yaml._load_yaml(local_path + 'path.yml')
    config.path_bet = path['bet']
    config.path_model = path['model']
    config.path_races = path['races']
    config.path_result = path['result']
    config.path_setting = path['setting']
    config.path_statistics = path['statistics']


def _investment():

    path = load_yaml._load_yaml(local_path + 'path.yml')
    config.path_investment = path['investment']


def _transscript():

    path = load_yaml._load_yaml(local_path + 'path.yml')
    config.path_transscript = path['transscript']
