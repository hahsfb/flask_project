# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 上午10:25
# @Author  : HQJ
# @Site    :
# @File    : run.py

from app.run import create_app
from werkzeug.exceptions import HTTPException
from app.comm.error_base import APIException
from flask import request
from app.comm.log import Log
from flask_apscheduler import APScheduler
from app.service.v1.test import get_for_html


# create scheduler
scheduler=APScheduler()

app = create_app()
app.config.from_object('app.setting')
app.config['SCHEDULER_API_ENABLED'] = True


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        data = []
        return APIException(msg, code, data)
    else:
        if not app.config['DEBUG']:
            return APIException(msg="系统异常错误")
        else:
            return e


@app.before_request
def before_request():
    Log.info('-' * 50)
    Log.info('[RequestUrl:] %s' % request)


@app.after_request
def after_request(response):
    Log.info('-' * 50)
    return response


if __name__ == '__main__':
    scheduler.init_app(app)
    # scheduler.add_job(func=get_for_html, args=(app,), trigger='cron', hour='00', minute='00', second='00', id='job_1')
    scheduler.add_job(func=get_for_html, trigger='interval', seconds=app.config['SLEEP_TIME'], id='job_2')
    Log.info('scheduler开始。。。。')
    scheduler.start()
    app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'])
