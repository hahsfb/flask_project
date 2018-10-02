#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 上午10:21
# @Author  : HQJ
# @Site    :
# @File    : run.py
from flask import Flask
from flask import Flask as New_Flask
from flask.json import JSONEncoder as _JSONEncoder
from datetime import date
from decimal import *
from app.service.v1.test import test
# from app.app.models import db


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(o, Decimal):
            return round(float(o), 2)
        try:
            return o.value
        except:
            return None


class Flask(New_Flask):
    json_encoder = JSONEncoder


def register_blueprints(app):
    '''
    registration route (module)
    :param app:
    :return:
    '''
    # 商户端蓝图
    app.register_blueprint(test)


def migrations_table(app):
    '''
    new database_tables
    :param app:
    :return:
    '''
    # 商户端迁移
    # from app.app.models import db
    # db.init_app(app=app)


def create_app():
    '''
    entry
    :return:
    '''
    app = Flask(__name__)
    app.config.from_object('app.setting')

    # session配置 加密:urandom(24) 有效时间:15分钟
    # app.config['SECRET_KEY'] = urandom(24)
    # app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)

    # 蓝图执行处
    register_blueprints(app)
    # 迁移执行处
    # migrations_table(app)
    # db.init_app(app)

    return app
