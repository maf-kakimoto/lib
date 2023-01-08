# -*- coding: utf-8 -*-

import csv
from ruamel.yaml import YAML, add_constructor, resolver
from collections import OrderedDict


def _f2f(input, output):

    add_constructor(
        resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        lambda loader,
        node: OrderedDict(loader.construct_pairs(node))
        )

    yaml = YAML()
    yaml.default_flow_style = False

    list = []
    with open(input, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            list.append(row)

    with open(output, encoding='utf-8', mode='w') as f:
        yaml.dump(list, f)
