#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = "meiming"

# email : 260548893@qq.com

import urllib2
import re
import json
import traceback
from server_info import ServerInfo

class AutoConfig(object):
    def __init__(self, serverUrl, configFile):
        self.mServerUrl = serverUrl
        self.mConfigFile = configFile


    @staticmethod
    def getHtml(url):
        '''
        根据url获取对应html
        :param url:网址
        :return:
        '''
        html = None
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            contentBytes = response.read()
            html = contentBytes.decode('utf-8')
        except:
            print "get html from %s error!" %url
            traceback.print_exc()
        return html


    @staticmethod
    def getServerInfo(html):
        '''
        根据html获取代理服务器信息
        :param html: 获得的网页html
        :return: 服务器信息
        '''
        #通过正在匹配，定位免费服务器信息块
        patternFree = re.compile(r"<!-- Free SS Section -->(.*?)<!-- Provider list Section -->",re.S)
        shadowsocksSection = re.findall(patternFree, html)
        #print shadowsocksSection

        #通过正则，更加精确的找到免费服务器对应的div
        patternDiv = re.compile(r"<div class=\"col-sm-4 text-center\">(.*?)</div>", re.S)
        serverInfoDivs = re.findall(patternDiv, shadowsocksSection[0])
        #print serverInfoDivs

        itemList = []
        #遍历存在的三个服务器对象
        for serverInfoDiv in serverInfoDivs:
            #通过正则查找匹配的服务器每项信息
            patternServerInfoItems = re.compile(r"<h4>(.*?)</h4>", re.S)
            serverInfoItems = re.findall(patternServerInfoItems, serverInfoDiv)
            #print serverInfoItems

            itemList = []
            for si in serverInfoItems:
                item = si.split(":")
                #print item

                # 过滤没有：的项
                if len(item) < 2:
                    continue

                #获取的内容加入列表
                itemList.append(item[1])

            #如果密码不为空，找到了可用服务器信息
            if len(itemList[2]) != 0:
                break

        #组装代理服务器信息
        server = itemList[0]
        server_port = int(itemList[1])
        local_address = "127.0.0.1"
        local_port = 1080
        password = itemList[2]
        timeout= 300
        method = itemList[3]
        fast_open = True

        #实例化服务器信息类
        serverInfo = ServerInfo(server, server_port,local_address,local_port, password,timeout,method,fast_open)

        return serverInfo


    @staticmethod
    def writeToConfigFile(info, fileName):
        '''
        把代理服务器信息写入配置文件
        :param info:代理服务器信息
        :param fileName:配置文件名
        :return:
        '''
        with open(fileName, "w") as file:
            json.dump(info.toDict(), file)


    def run(self):
        '''
        运行程序，自动获取代理服务器信息，并写入配置文件
        :return:
        '''
        html = AutoConfig.getHtml(self.mServerUrl)
        if html != None:
            print u"成功获取网页内容!"
            #print html
            serverInfo = None
            try:
                # 获取服务信息
                serverInfo = AutoConfig.getServerInfo(html)
                print u"成功获取服务器信息！"

                # 服务器信息写入对应配置文件
                AutoConfig.writeToConfigFile(serverInfo, self.mConfigFile)
                print u"代理服务器信息成功写入配置文件！"
            except:
                print u"获取服务器信息异常，需要更新脚本！"
                traceback.print_exc()


if __name__ == "__main__":
    # 提供免费代理服务器的地址
    #serverUrl = "http://www.ishadowsocks.org/"
    serverUrl = "https://b.ishadow.tech/"

    # 配置文件存放位置
    configFile = "/home/meiming/ss_conf.json"

    autoConfig = AutoConfig(serverUrl, configFile)
    autoConfig.run()
