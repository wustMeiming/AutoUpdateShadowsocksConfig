#!/usr/bin/env python2
# -*- coding: utf-8 -*-
class ServerInfo(object):

    def __init__(self, server, server_port,local_address,local_port, password,timeout,method,fast_open):
        """
        server      你服务端的IP
        server_port 你服务端的端口
        local_port  本地端口，一般默认1080
        password    ss服务端设置的密码
        timeout     超时设置和服务端一样
        method      加密方法和服务端一样
        """
        self.server = server
        self.server_port = server_port
        self.local_address = local_address
        self.local_port = local_port
        self.password = password
        self.timeout = timeout
        self.method = method
        self.fast_open = fast_open

    def dump(self):
        print self.toDict()

    def toDict(self):
        info={}
        info["server"]=self.server
        info["server_port"]=self.server_port
        info["local_address"]=self.local_address
        info["password"]=self.password
        info["timeout"]=self.timeout
        info["method"]=self.method
        info["fast_open"]=self.fast_open
        return info