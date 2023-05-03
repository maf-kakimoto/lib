# -*- coding: utf-8 -*-

import pymysql.cursors


def _connect():

    con = pymysql.connect(
        host='xxx',
        db='xxx',
        user='xxx',
        password='xxx'
        )
    cur = con.cursor()

    return con, cur


def _end(con):

    con.commit()
    con.close()
