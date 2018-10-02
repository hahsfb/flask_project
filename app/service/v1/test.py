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


@test.route('/v1/checkOrderExist', methods=['GET', 'POST'])
def check_order_exist():
    return jsonify({"data": "ok"})


def get_for_html():
    with open('story.json', mode='r', encoding='utf-8')as f:
        data = json.load(f)
        for item in data.get('data'):
            result = get_text(item.get('name'), item.get('domain_name'), item.get('url'), item.get('latest_chapter'))
            if result:
                item['latest_chapter'] = result
            Log.info('%s 检查完毕。。。' % item.get('name'))

    with open('story.json', mode='w', encoding='utf-8')as f:
        f.write(json.dumps(data))
        Log.info('json更新完毕。。。')
    Log.info('全部检查完毕')
    Log.info("---" * 20)
    # Log.info(processbar3(10*60))
