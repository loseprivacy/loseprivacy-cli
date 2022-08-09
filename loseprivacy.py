#!/usr/bin/python3
# coding=utf-8
#
#  LosePrivacy API，最全最强大的社工库平台
#  官网：https://loseprivacy.click
#  API介绍：https://loseprivacy.github.io
#  CopyRight 2022 LosePrivacy.
#

import os
import requests
import json
import time
import logging


class LosePrivacy():
    # 可搜索的数据类别
    dataclasses = {}
    # 不同类别下的数据泄露事件：cate:breach
    breach_map = {}
    # 所有数据泄露事件：breach_id:breach
    all_breaches = {}
    # 所有数据泄露专题: topic_id:topic
    all_topics = {} 

    host = 'https://api.loseprivacy.cyou'
    key = 'loseprivacy_apikey'
    ratelimit = 2
    timeout = 60

    url_dc = '/api/v1/dataclasses'
    url_breaches = '/api/v1/breaches'
    url_breach = '/api/v1/breach'
    url_searchbreach = '/api/v1/search_breach'
    url_topics = '/api/v1/topics'
    url_topic = '/api/v1/topic'
    url_searchtopic = '/api/v1/search_topic'

    file_dc = "loseprivacy/loseprivacy_dataclasses.txt"
    file_breachmap = "loseprivacy/loseprivacy_breach_map.txt"
    file_breaches = "loseprivacy/loseprivacy_breaches.txt"
    file_topics = "loseprivacy/loseprivacy_topics.txt"

    def __init__(self, gateway, key, ratelimit, timeout=60, log_level=logging.INFO):
        self.host = gateway
        self.key = key
        self.ratelimit = ratelimit
        self.timeout = timeout
        logging.basicConfig(level=log_level, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    def header(self):
        headers = {
            'User-Agent': 'loseprivacy',
            'loseprivacy-auth-key': self.key,
        }
        return headers

    # 从LosePrivacy拉取基本的数据泄露事件的数据并存入文件中
    def init_data(self):
        if os.path.exists(self.file_dc) and os.path.exists(self.file_breachmap) and os.path.exists(self.file_breaches) and os.path.exists(self.file_topics):
            return
        if not os.path.exists('loseprivacy'):
            os.mkdir('loseprivacy')
        logging.info('首次运行，将从LosePrivacy服务器中拉取最新的数据泄露事件的元数据')
        # 获取LosePrivacy所有可搜索的数据类别
        self.dataclasses = self.get_dataclasses()
        # 获取LosePrivacy每一类别的数据泄露事件的具体信息
        for dataclass in self.dataclasses:
            breaches = self.get_breaches(dataclass['field'])
            self.breach_map[json.dumps(dataclass)] = breaches
            logging.info('%s类别下的数据泄露事件有：' % dataclass['name'])
            for breach in breaches:
                logging.info('%s:%s' % (breach['name'], breach['title']))
                self.all_breaches[breach['id']] = breach
        # 获取LosePrivacy所有数据泄露专题信息
        all_topics = self.get_topics()
        with open(self.file_dc, 'w+') as dc_file:
            dc_file.write(json.dumps(self.dataclasses))
        with open(self.file_breachmap, 'w+') as breach_file:
            breach_file.write(json.dumps(self.breach_map))
        with open(self.file_breaches, 'w+') as breaches_file:
            breaches_file.write(json.dumps(self.all_breaches))
        with open(self.file_topics, 'w+') as topics_file:
            topics_file.write(json.dumps(all_topics))

    # 后续运行时可以直接使用
    def load_data(self):
        if os.path.exists(self.file_dc) and os.path.exists(self.file_breachmap) and os.path.exists(self.file_breaches) and os.path.exists(self.file_topics):
            with open(self.file_dc) as f:
                data = f.read()
                self.dataclasses = json.loads(data)
            with open(self.file_breachmap) as f:
                data = f.read()
                self.breach_map = json.loads(data)
            with open(self.file_breaches) as f:
                data = f.read()
                self.all_breaches = json.loads(data)
            with open(self.file_topics) as f:
                data = f.read()
                all_topics = json.loads(data)
            return
        logging.error('load_data错误：请先调用init_data()，再调用load_data()!')
    
    # 获取LosePrivacy所有可搜索的数据类别
    def get_dataclasses(self):
        rsp = requests.post(url = self.host+self.url_dc, data = {},headers = self.header(), timeout=self.timeout)
        obj = json.loads(rsp.text.strip())
        time.sleep(self.ratelimit)
        if obj['code'] == 200:
            logging.info('LosePrivacy可搜索的数据类型：')
            for cate in obj['data']:
                logging.info('%s: field_name:%s, field_value:%s' % (cate['name'],cate['field'],cate['value']))
            return obj['data']
        else:
            return None

    # 获取LosePrivacy某一类别的数据泄露事件
    def get_breaches(self, field):
        rsp = requests.post(url = self.host+self.url_breaches, data = {'field':field},headers = self.header(), timeout=self.timeout)
        obj = json.loads(rsp.text.strip())
        time.sleep(self.ratelimit)
        if obj['code'] == 200:
            return obj['data']
        else:
            return None

    # 获取LosePrivacy的所有数据泄露专题
    def get_topics(self):
        rsp = requests.post(url = self.host+self.url_topics, data = {},headers = self.header(), timeout=self.timeout)
        obj = json.loads(rsp.text.strip())
        time.sleep(self.ratelimit)
        if obj['code'] == 200:
            return obj['data']
        else:
            return None

    # 搜索泄露信息
    def searchbreach(self,keyword,breach_id,field):
        data = {'keyword':keyword,'breach_id':breach_id,'field_value':field}
        rsp = requests.post(url = self.host+self.url_searchbreach, data = data,headers = self.header(), timeout=self.timeout)
        obj = json.loads(rsp.text.strip())
        time.sleep(self.ratelimit)
        if obj['code'] == 200:
            return obj['data']
        else:
            return None

    def search(self,keyword,field_value):
        cates = self.breach_map.keys()
        qq_cate = None
        qq_cate_str = None
        result = {}
        for cate in cates:
            qq_cate_str = cate
            cate = json.loads(cate)
            if cate['value'] == field_value:
                qq_cate = cate
                break
        for breach in self.breach_map[qq_cate_str]:
            logging.info('正在搜索%s-%s, 关键词:%s' % (breach['id'],breach['title'],keyword))
            res = self.searchbreach(keyword,breach['id'],qq_cate['value'])
            if len(res) > 0:
                result[breach['title']] = res
        return result

    def search_qq(self, keyword):
        logging.info('正在搜索QQ %s' % keyword)
        return self.search(keyword,'qq')

    def search_username(self,keyword):
        logging.info('正在搜索用户名 %s' % keyword)
        return self.search(keyword,'username')

    def search_password(self,keyword):
        logging.info('正在搜索密码 %s' % keyword)
        return self.search(keyword,'password')

    def search_phone(self,keyword):
        logging.info('正在搜索手机 %s' % keyword)
        return self.search(keyword,'phone')

    def search_identity(self,keyword):
        logging.info('正在搜索身份证号 %s' % keyword)
        return self.search(keyword,'identity')

    def search_weiboid(self,keyword):
        logging.info('正在搜索微博UID %s' % keyword)
        return self.search(keyword,'weibo')

    def search_facebook(self,keyword):
        logging.info('正在搜索Facebook ID %s' % keyword)
        return self.search(keyword,'facebook')

    def search_email(self,keyword):
        logging.info('正在搜索邮箱 %s' % keyword)
        return self.search(keyword,'email')

    def dump(self):
        for key in self.all_breaches.keys():
            breach = self.all_breaches[key]
            logging.info('%s:%s' % (breach['name'], breach['title']))

