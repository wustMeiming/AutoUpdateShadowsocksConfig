#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import re
import json
import ServerInfo

url = 'http://www.ishadowsocks.com/'

req = urllib2.Request(url)

try:
    response=urllib2.urlopen(req)
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
else:
    print "OK"

html = response.read().decode('utf-8')
#print html
pattern = re.compile(r'<!-- Free Shadowsocks Section -->(.*?)<!-- Provider list Section -->',re.S)

result = re.findall(pattern, html)
#print result

p = re.compile(r'<div class="col-lg-4 text-center">(.*?)</div>', re.S);
r = re.findall(p, result[0])

#print r

p1=re.compile(r'<h4>(.*?)</h4>',re.S)
r1=re.findall(p1, r[0])

p2=re.compile(r':', re.S)
info=[]
for i in r1:
    ret = re.split(p2,i)
    if ret.__len__() < 2:
        continue
    info.append(ret[1])
    #print ret[0] + "  " + ret[1]

server = info[0]
server_port = int(info[1])
local_address = '127.0.0.1'
local_port = 1080
password = info[2]
timeout= 300
method = info[3]
fast_open = True
obj = ServerInfo.ServerInfo(server, server_port,local_address,local_port, password,timeout,method,fast_open)
json.dump(obj.toDict(), open('/home/meiming/apps/ss_conf.json', 'w'))

#data=json.load(open('/home/meiming/apps/ss_conf.json', 'r'))
#print data
