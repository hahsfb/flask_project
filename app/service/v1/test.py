#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : test.py
@Author  : HaoQiangJian
@Site    :
@Time    : 18-9-20 下午12:03
@Version :
"""
import json
from . import test
from flask import jsonify
from app.comm.get_form_html import get_text
from app.comm.log import Log
from app.setting import FILE_PATH


@test.route('/', methods=['GET', 'POST'])
def check_order_exist():
    return jsonify({"data": "ok"})


@test.route('/get', methods=['GET'])
def get_for_html():
    with open(FILE_PATH, mode='r', encoding='utf-8')as f:
        data = json.load(f)
        for item in data.get('data'):
            result = get_text(item.get('name'), item.get('domain_name'), item.get('url'), item.get('latest_chapter'))
            if result:
                item['latest_chapter'] = result
            Log.info('%s 检查完毕。。。' % item.get('name'))

    with open(FILE_PATH, mode='w', encoding='utf-8')as f:
        f.write(json.dumps(data))
        Log.info('json更新完毕。。。')
    Log.info('全部检查完毕')
    Log.info("---" * 20)
    return jsonify({"data": "全部检查完毕"})


# def get_for_html():
#     with open(FILE_PATH, mode='r', encoding='utf-8')as f:
#         data = json.load(f)
#         for item in data.get('data'):
#             result = get_text(item.get('name'), item.get('domain_name'), item.get('url'), item.get('latest_chapter'))
#             if result:
#                 item['latest_chapter'] = result
#             Log.info('%s 检查完毕。。。' % item.get('name'))
#
#     with open(FILE_PATH, mode='w', encoding='utf-8')as f:
#         f.write(json.dumps(data))
#         Log.info('json更新完毕。。。')
#     Log.info('全部检查完毕')
#     Log.info("---" * 20)
    # Log.info(processbar3(10*60))
