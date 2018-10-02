#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/7 下午7:50
# @Author  : Nikky
# @Site    : 
# @File    : requests.py
import requests
from flask import jsonify


class Request:

    @staticmethod
    def get(url, return_json=False):
        '''
        发送get请求
        :param url:
        :param return_json:
        :return:
        '''
        try:
            r = requests.get(url=url)
            if r.status_code != 200:
                return {} if return_json else ''
            else:
                return r.json() if return_json else r.text
        except:
            return False

    @staticmethod
    def post(url, data={}, return_json=False):
        '''
        发送post请求
        :param url:
        :param data:
        :param return_json:
        :return:
        '''
        try:
            pass
        except Exception as e:
            pass


if __name__ == '__main__':
    content = Request.get('http://www.baidu.com')
    print(content)
