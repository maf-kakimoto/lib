# -*- coding: utf-8 -*-

import pandas as pd


def _f2f(input, output):

    data = pd.read_excel(input, index_col=None)
    data.to_csv(output, encoding='utf-8')


def _s2df(input, sheet, skiprows):

    df = pd.read_excel(input, sheet_name=sheet, skiprows=skiprows, index_col=None)

    return df
