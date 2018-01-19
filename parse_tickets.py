#coding=utf-8
import re
import requests
from pprint import pprint

url="https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9044"
res=requests.get(url,verify=False)
patten=u"([\u4e00-\u9fa5]+)\|([A-Z]+)"
stations=re.findall(patten,res.text)
pprint(dict(stations),indent=4)
#print(stations)