# -*- coding:utf-8 -*-
from flask import Flask, render_template, request
import pymysql as mysql
import json

con = mysql.connect(user="root", passwd="123456", db="mem", host="192.168.2.22")
con.autocommit(True)
cur = con.cursor()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getdata')
def getdata():
    lasttime = request.args.get('lasttime')
    sql = 'select * from mem_used'
    if lasttime:
        sql += ' where time > %s' % (lasttime)
    print(sql)
    cur.execute(sql)
    arr = []
    for i in cur.fetchall():
        arr.append({'name': i[1], 'value': [i[1], i[0]]})
    all_res = {'data': arr}
    all_res['max_time'] = arr[-1]['name']
    return json.dumps(all_res)

@app.route('/getdatas')
def getdatas():
    sql = 'select * from mem_used'
    cur.execute(sql)
    arr = []
    for i in cur.fetchall():
        arr.append({'name': i[1], 'value': [i[1], i[0]]})
    return json.dumps(arr)


if __name__ == '__main__':
    app.run(debug=True)
