# -*- coding:utf-8 -*-

import csv
import pandas as pd


def _load_as_dic(file):

    csvfile = open(file, 'r')
    dataDIC = csv.DictReader(csvfile)

    return dataDIC


def _load_as_df(file):

    csvfile = open(file, 'r')
    dataDF = pd.read_csv(csvfile)

    return dataDF


def _load_as_csv(file):

    csvfile = open(file, 'r')
    dataCSV = csv.reader(csvfile)

    return dataCSV
