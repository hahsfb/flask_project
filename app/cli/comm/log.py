#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : redis.py
@Author  : HaoQiangJian
@Site    :
@Time    : 18-9-20 下午12:03
@Version :
"""
import os
from app.cli.setting import *
import time
from logzero import logging, setup_logger


class Log:

    @staticmethod
    def info(message):
        if not os.path.isdir(LOGS_DIR):
            os.makedirs(LOGS_DIR)
        logger_obj = setup_logger(
            logfile=LOGS_DIR + time.strftime("%Y-%m-%d", time.localtime()) + '-info.log',
            level=logging.INFO)

        if not message:
            message = ""
        logger_obj.info(message)

    @staticmethod
    def debug(message):
        if not os.path.isdir(LOGS_DIR):
            os.makedirs(LOGS_DIR)
        logger_obj = setup_logger(
            logfile=LOGS_DIR + time.strftime("%Y-%m-%d", time.localtime()) + '-debug.log',
            level=logging.DEBUG)

        if not message:
            message = ""
        logger_obj.debug(message)
