# -*- coding: utf-8 -*-
# @Time    : 2024/6/4 12:56
# @Author  : name
# @File    : test_time.py

import requests
import pytest

def test_baidu():
    r=requests.get(url='http://www.baidu.com/')
    print(r.elapsed.total_seconds())
    print(r.cookies.items())
    assert r.status_code==200

def test_taobao():
    r=requests.get(url='http://taobao.com/')
    print(r.elapsed.total_seconds())
    assert r.status_code==200

def test_jd():
    r=requests.get(url='http://jd.com/')
    print(r.elapsed.total_seconds())
    assert r.status_code==200

@pytest.mark.flaky(reruns=3,reruns_delay=5)
def test_weibo():
    r=requests.get(url='http://weibo.com/',timeout=0.1)
    print(r.elapsed.total_seconds())
    assert r.status_code==200