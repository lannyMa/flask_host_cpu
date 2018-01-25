#!/usr/bin/env python
# coding=utf-8

## 1, 获取内存  2,入库
import pymysql
from time import time, sleep
import psutil

con = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mem')
con.autocommit(True)
cur = con.cursor()


def get_mem():
    free = psutil.virtual_memory().free / 1024 / 1024
    sql = "insert into mem_used VALUES(%s,%s)" % (free, int(time()))
    cur.execute(sql)



while True:
    get_mem()
    sleep(1)
