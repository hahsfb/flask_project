#! -coding:utf8 -*-
import os
import sys
import threading
import time

import requests


class MulThreadDownload(threading.Thread):
    def __init__(self, url, startpos, endpos, f):
        super(MulThreadDownload, self).__init__()
        self.url = url
        self.startpos = startpos
        self.endpos = endpos
        self.fd = f

    def download(self):
        print("start thread:%s at %s" % (self.getName(), time.time()))
        headers = {"Range": "bytes=%s-%s" % (self.startpos, self.endpos)}
        res = requests.get(self.url, headers=headers)
        # res.text 是将get获取的byte类型数据自动编码，是str类型， res.content是原始的byte类型数据
        # 所以下面是直接write(res.content)
        self.fd.seek(self.startpos)
        self.fd.write(res.content)
        print("stop thread:%s at %s" % (self.getName(), time.time()))
        # f.close()

    def run(self):
        self.download()


def file_download(filename):
    # 流式读取
    store_path = './upload/%s' % filename
    with open(store_path, 'rb') as target_file:
        while True:
            chunk = target_file.read(20 * 1024 * 1024)  # 每次读取20M
            if not chunk:
                break
            yield chunk
    # return Response(send_chunk(), content_type='application/octet-stream')


def down_method1(url):
    # url = sys.argv[1]
    # url = 'https://cd.phncdn.com/videos/201803/13/157946062/720P_1500K_157946062.mp4?MXZP8MO0rVNukDSdD_-CfZVXE21X50L7JcqZ2onC-5xLdgKgc6OYSXLstwcEgADJe86zI15ifUlll1U9uV90gOqE0FjrfyG7409801yUXyyEYfCly7sxKDHhVMuuP4xQ1ohN5d1Ly2MbodKXHWUhENJJa1rhPtiSWMcb4Tr35rlgfACxke_PoEftfDgP8QBjd3kLB77iYr-_'
    # 获取文件的大小和文件名
    # filename = url.split('/')[-1]
    filename = '480P_600K_110031752.mp4'
    filesize = int(requests.head(url).headers['Content-Length'])
    print("%s filesize:%s" % (filename, filesize))

    # 线程数
    threadnum = 20
    # 信号量，同时只允许3个线程运行
    threading.BoundedSemaphore(threadnum)
    # 默认3线程现在，也可以通过传参的方式设置线程数
    step = filesize // threadnum
    mtd_list = []
    start = 0
    end = -1

    # 请空并生成文件
    tempf = open(filename, 'w')
    tempf.close()
    # rb+ ，二进制打开，可任意位置读写
    with open(filename, 'rb+') as  f:
        fileno = f.fileno()
        # 如果文件大小为11字节，那就是获取文件0-10的位置的数据。如果end = 10，说明数据已经获取完了。
        while end < filesize - 1:
            start = end + 1
            end = start + step - 1
            if end > filesize:
                end = filesize
            # print("start:%s, end:%s"%(start,end))
            # 复制文件句柄
            dup = os.dup(fileno)
            # print(dup)
            # 打开文件
            fd = os.fdopen(dup, 'rb+', -1)
            # print(fd)
            t = MulThreadDownload(url, start, end, fd)
            t.start()
            mtd_list.append(t)

        for i in mtd_list:
            i.join()


def down_method2(url):
    import requests
    # url = "http://hjwachhy.site/game/only_v1.1.1.apk"
    path = "./download/xx.mp4"
    r = requests.get(url)
    print('ok')
    with open(path, "wb") as f:
        f.write(r.content)
    f.close()


if __name__ == "__main__":
    url = 'https://cd.phncdn.com/videos/201808/12/178253991/720P_1500K_178253991.mp4?GpJFspWZMHs75c_dAxIr0OvYmZ_LWE9d5TUfHt4inlMCdrUC6f1L_b8DGn1wCx0PWIIlsQQKcSlsZbIuAhcsMbhLlanDcWKrknEryKkmj1edQfMRGlopZKdtOPhdakUnAM2Wc4OMapjOJCfLcTvYP5UtgcqrvsGdI5ESpOm7IpboXeMNgD48q4VeXlFme-JO9tziwGYM8jtUEw'

    down_method1(url)
    # down_method2(url)
    # file_download(url)

