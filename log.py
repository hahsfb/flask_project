#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/8 上午1:18
# @Author  : Nikky
# @Site    : 
# @File    : log.py
import os
import time
from logzero import logging, setup_logger

LOGS_DIR = "./logData"


class log:

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
