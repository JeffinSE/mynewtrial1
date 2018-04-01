#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2018-03-29 19:33
@Author  : Jeff
@Email   : xiajihong75@gmail.com
@Software: PyCharm
@File    : testof@.py
@license : (C) Copyright 2018, xxx Limited.
@Site    : http://github.com
@Description: 
'''


def a(fn):
    'aaa doc'
    print('print aaa firstly')

    def d(st):
        print(st + ' new func')
    return d


def b(fn):
    print('b only')
    return fn


@a
def c(st):
    print(st)


if __name__ == '__main__':
    c('ccc')
    c('ttt')

