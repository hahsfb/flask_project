#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : progress.py
@Author  : HaoQ iangJian
@Site    : 
@Time    : 18-9-17 下午1:26
@Version : 
"""

import time
from progressbar import *
# progressbar安装: pip install progressbar

from tqdm import tqdm, trange
# tqdm安装: pip install tqdm


total = 100


def processbar0():
    d = 0
    for data in range(1, 11):
        time.sleep(0.2)
        d += 1
        done = int(50 * d / 10)
        sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 10 * d))
        sys.stdout.flush()


# ===================================progressbar=====================================
def dosomework():
    time.sleep(0.01)


def processbar1():
    """
    方法一: progressbar
    :return:  100% |#########################################################################|
    """
    bar = ProgressBar()
    for i in bar(range(total)):
        dosomework()



def processbar2():
    """
    方法二: progressbar
    :return:  100% |#########################################################################|
    """
    pbar = ProgressBar().start()
    for i in range(total):
        pbar.update(int((i / (total - 1)) * 100))
        dosomework()
    pbar.finish()


def processbar3(total):
    """
    方法三: progressbar
    :return:  Progress: 100% |###############| Elapsed Time: 0:00:01 Time: 0:00:01 953.91  B/s

    widgets可选参数含义：
        'Progress:'：设置进度条前显示的文字
        Percentage()：显示百分比
        Bar('#') ： 设置进度条形状
        ETA() ： 显示预计剩余时间
        Timer() ：显示已用时间
    """
    widgets = ['Progress: ', Percentage(), ' ', Bar('#'), ' ', Timer(),
               ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=total).start()
    for i in range(total):
        # do something
        pbar.update(i + 1)
        dosomework()
    pbar.finish()


# ===================================tqdm=====================================
# https://blog.csdn.net/langb2014/article/details/54798823?locationnum=8&fps=1
def tqdm1():
    """
    方法1: tqdm

    :return:  23%|████████▌                             | 2260/10000 [00:23<01:19, 97.83it/s]
    """
    for i in tqdm(range(total)):
        time.sleep(0.01)


def tqdm2():
    """
    方法2: tqdm

    :return:  23%|████████▌                             | 2260/10000 [00:23<01:19, 97.83it/s]
    """
    for i in trange(total):
        time.sleep(0.1)


def tqdm3():
    """
    方法3: tqdm

    :return:  23%|████████▌                             | 2260/10000 [00:23<01:19, 97.83it/s]
    """
    pbar = tqdm(["a", "b", "c", "d"])
    for char in pbar:
        pbar.set_description("Processing %s" % char)


def tqdm4():
    """
    方法4: tqdm

    :return:  23%|████████▌                             | 2260/10000 [00:23<01:19, 97.83it/s]
    """
    with tqdm(total=total) as pbar:
        for i in range(10):
            pbar.update(10)


if __name__ == '__main__':
    # processbar0()
    # processbar1()
    # processbar2()
    processbar3(60)

    # tqdm1()
    # tqdm2()
    # tqdm3()
    # tqdm4()
