# -*- coding: utf-8 -*-

import yaml


def _load_yaml(file):

    with open(file, mode='r') as yamlfile:

        data = yaml.load(stream=yamlfile, Loader=yaml.SafeLoader)

        return data
