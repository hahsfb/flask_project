#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
import requests
# import urllib2

my_sender = 'haohsfb@126.com'  # 发件人邮箱账号
my_pass = 'hao521912'  # 发件人邮箱密码
my_user = 'haohsfb@126.com'  # 收件人邮箱账号，我这边发送给自己


def mail(name, title, content):
    global server
    ret = True
    mail_msg = content
    try:
        msg = MIMEText(mail_msg, 'html', 'utf-8')
        msg['From'] = formataddr([name, my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["haohsfb", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = title  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.126.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(e)
        ret = False
    finally:
        server.close()  # 关闭连接
    return ret

#
# if __name__ == '__main__':
#     ret = mail("test", 'test', '<p>test<p>')
#     if ret:
#         print("邮件发送成功")
#     else:
#         print("邮件发送失败")
