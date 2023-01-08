# -*- coding:utf-8 -*-

from lib import manage_mysql


def _select(table, conditionDict={}, columnList=['*']):

    query = 'SELECT '
    for column in columnList:
        query += column + ','
    query = query[:-1]
    query += ' from ' + table

    if len(conditionDict) > 0:
        query += ' where '
        i = 0
        for key in conditionDict:
            if i != 0:
                query += ' and '
            query += key + '=' + conditionDict[key]
            i += 1

    return query


def _count(table, conditionDict={}):

    query = 'SELECT count(*) '
    query += 'from ' + table + ' '

    if len(conditionDict) > 0:
        query += 'where '
        i = 0
        for key in conditionDict:
            if i != 0:
                query += ' and '
            query += key + '=' + conditionDict[key]
            i += 1

    return query


def _distinct(table, column):

    query = 'SELECT distinct ' + column
    query += ' from ' + table

    return query


def _insert_from_List(table, valueList):

    values = ''
    for value in valueList:
        values += '"' + value + '",'
    values = values[:-1]

    query = 'INSERT INTO ' + table + ' '
    query += 'VALUES ('
    query += values
    query += ')'

    return query


def _insert_from_Dict(table, valueDict):

    columns = ''
    values = ''
    for key in valueDict:
        columns += key + ','
        values += '"' + valueDict[key] + '",'
    columns = columns[:-1]
    values = values[:-1]

    query = 'INSERT INTO ' + table + ' '
    query += '('
    query += columns
    query += ') '
    query += 'VALUES '
    query += '('
    query += values
    query += ')'

    return query


def _update(table, valueDict, conditionDict):

    value = ''
    for key in valueDict:
        value += key + '=' + valueDict[key] + ','
    value = value[:-1]

    condition = ''
    for key in conditionDict:
        condition += key + '=' + conditionDict[key] + ' and '
    condition = condition[:-5]

    query = 'UPDATE ' + table
    query += ' SET ' + value
    query += ' WHERE ' + condition

    return query


def _delete(table):

    con, cur = manage_mysql._connect()

    sql = 'DELETE from ' + table
    cur.execute(sql)

    manage_mysql._end(con)


def _create(table, columnList, type):

    con, cur = manage_mysql._connect()

    sql = 'CREATE table ' + table
    sql += ' ('
    for column in columnList:
        sql += column + ' ' + type + ','
    sql = sql[:-1]
    sql += ')'
    cur.execute(sql)

    manage_mysql._end(con)


def _drop(table):

    con, cur = manage_mysql._connect()

    sql = 'DROP table if exists ' + table
    cur.execute(sql)

    manage_mysql._end(con)
