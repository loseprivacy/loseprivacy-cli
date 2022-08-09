#!/usr/bin/python3
# coding=utf-8
#
#  LosePrivacy API Sample，最全最强大的社工库平台
#  官网：https://loseprivacy.click
#  API介绍：https://loseprivacy.github.io
#  CopyRight 2022 LosePrivacy.
#

import os
import requests
import json
import time
import logging
from loseprivacy import LosePrivacy

host = 'https://api.loseprivacy.cyou'
apikey = '填入从LosePrivacy获取的API KEY'
ratelimit = 2
timeout = 60

def main():
    lp = LosePrivacy(host,apikey,ratelimit,timeout,logging.INFO)
    lp.init_data()
    lp.load_data()
    res = lp.search_qq("2118558610")
    print(res)

if __name__ == "__main__":
        main()

