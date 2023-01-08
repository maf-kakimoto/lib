# -*- coding: utf-8 -*-

import pymysql.cursors


def _connect():

    con = pymysql.connect(
        host='localhost',
        db='keiba',
        user='root',
        password=''
        )
    cur = con.cursor()

    return con, cur


def _end(con):

    con.commit()
    con.close()
