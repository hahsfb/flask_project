#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : redis.py
@Author  : HaoQiangJian
@Site    : 
@Time    : 18-9-20 下午12:03
@Version : 
"""
import hashlib
import string, random
from app.cli.comm.log import Log


def true_return(data='', msg='请求成功', code=200):
    data = {
        "code": code,
        "msg": msg,
        "data": data
    }
    Log.info('[ResponseData:] %s' % data)
    return data


def true_return_pagination(pagination=None, data=None, msg='请求成功', code=200):
    data = {
        "pagination": pagination,
        "code": code,
        "msg": msg,
        "data": data
    }
    Log.info('[ResponseData:] %s' % data)
    return data


def false_return(data='', msg='请求失败', code=-1):
    data = {
        "code": code,
        "msg": msg,
        "data": data
    }
    Log.info('[ResponseData:] %s' % data)
    return data


def random_char(num):
    res = []
    for i in range(num):
        res.append(random.choice(string.ascii_letters + string.digits))
    return ''.join(res)


class Utils:
    '''
    * 用于sql结果列表对象类型转字典
    * @param list data
    * @return dict
    '''

    @staticmethod
    def db_l_to_d(data):
        data_list = []
        for val in data:
            val_dict = val.to_dict()
            data_list.append(val_dict)
        data = {}
        data = data_list
        return data

    ''' 
    * 用于sql结果对象类型转字典
    * @param object obj
    * @return dict
    '''

    @staticmethod
    def class_to_dict(obj):
        is_list = obj.__class__ == [].__class__
        is_set = obj.__class__ == set().__class__
        if is_list or is_set:
            obj_arr = []
            for o in obj:
                dict = {}
                dict.update(o.__dict__)
                obj_arr.append(dict)
                return obj_arr
        else:
            dict = {}
            dict.update(obj.__dict__)
            dict.__delitem__('_sa_instance_state')
            return dict


def tuple_to_dict(data, is_list=True):
    '''
    将tuple转化成dict
    :param data:
    :param is_list: 是否是list类型
    :return:
    '''
    if is_list:
        keys = data[0].keys()
        result = []
        for item in data:
            # print(item)
            result.append(dict(zip(keys, item)))
        return result
    else:
        keys = data.keys()
        return dict(zip(keys, data))


def class_to_list(obj):
    obj_list = []
    for item in obj:
        obj_list.append(Utils.class_to_dict(item))
    return obj_list


class CliUtils:

    @staticmethod
    def result(error_code=0, data=None, **kwargs):
        data = {
            "error_code": error_code,
            "data": data
        }
        for k, v in kwargs.items():
            data[k] = v
        Log.info('[ResponseData:] %s' % data)
        return data
