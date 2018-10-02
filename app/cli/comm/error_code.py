#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 上午10:07
# @Author  : Nikky
# @Site    : 
# @File    : error_code.py
from app.cli.comm.error_base import *


class ParameFail(APIException):
    code = 401
    data = []
    msg = "参数验证失败"


class TokenFail(APIException):
    code = 600
    data = []
    msg = "权限验证失败"


class ResultFail(APIException):
    code = 402
    data = []
    msg = "请求数据失败"


class ResultSuccess(APIException):
    code = 200
    data = []
    msg = "请求数据成功"
