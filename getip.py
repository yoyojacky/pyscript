#!/usr/bin/python
# 快速获取主机名与IP对应表.方便巡检及排错.

import urllib2
import json
import sys

reload(sys)
sys.setdefaultencoding(u'utf-8')

res=urllib2.urlopen("https://mypack.yoyojacky.com/device/server?jacky").read()

host = json.loads(res)

f = open("test.list","w")

for i in host:
    for ip_obj in i["outips"]:
        ip = ip_obj["ip"]
	name = i["hostname"]
	print ip+' '+name

f.write(ip+' '+name+"\n")
f.close()
