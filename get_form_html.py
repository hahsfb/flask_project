#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
import time
from bs4 import BeautifulSoup
from send_email import mail
from log import log
from progress import processbar3

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__jsluid=2f69fa9c6e3e78aea14586c79e354cc1',
    'Host': 'm.booktxt.net',
    'If-Modified-Since': 'Sun, 09 Sep 2018 03:58:10 GMT',
    'If-None-Match': 'W/"e7d8ab52f147d41:0"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}


def get_text(name, domain_name, story_addr, latest_chapter):
    req = requests.get(url=domain_name + story_addr, headers=header)
    encode_content = get_utf_8(req)
    new_latest_chapter = ''
    soup = BeautifulSoup(encode_content, 'html.parser')
    temp_list = []
    for link in soup.select(".directoryArea > p > a", limit=5):
        if link.get('href') != latest_chapter:
            temp_list.append(link.get('href'))
        elif link.get('href') == latest_chapter:
            break

    if temp_list:
        for single in reversed(temp_list):
            # 1.获取url网页内容
            title, content = text_detail(domain_name + single)
            # 2.发送邮件
            ret = mail(name, title, content)
            # ret = True
            if ret:
                new_latest_chapter = single
                print("邮件发送成功")
            else:
                print("邮件发送失败")
    return new_latest_chapter


def text_detail(url):
    req = requests.get(url, headers=header)
    html = get_utf_8(req)
    soup = BeautifulSoup(html, 'html.parser')
    for i in soup.select('.ReadAjax_content > p'):
        i.extract()
    title = soup.find('span').text
    # title = title.wrap(soup.new_tag("b"))
    # title = title.wrap(soup.new_tag("p"))
    content = soup.find('div', 'ReadAjax_content')
    # content.insert(0, title)
    return title, content


def get_utf_8(req):
    if req.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(req.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = req.apparent_encoding
        return req.content.decode(encoding, 'replace')  # 如果设置为replace，则会用?取代非法字符；


if __name__ == '__main__':
    while True:
        with open('story.json', mode='r', encoding='utf-8')as f:
            data = json.load(f)
            for item in data.get('data'):
                result = get_text(item.get('name'), item.get('domain_name'), item.get('url'), item.get('latest_chapter'))
                if result:
                    item['latest_chapter'] = result
                log.info('%s 检查完毕。。。' % item.get('name'))

        with open('story.json', mode='w', encoding='utf-8')as f:
            f.write(json.dumps(data))
            log.info('json更新完毕。。。')
        log.info('全部检查完毕')
        log.info("---" * 20)
        log.info(processbar3(10*60))
