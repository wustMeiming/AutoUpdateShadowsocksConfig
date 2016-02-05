class ServerInfo(object):

    def __init__(self, server, server_port,local_address,local_port, password,timeout,method,fast_open):
        self.server = server
        self.server_port = server_port
        self.local_address = local_address
        self.local_port = local_port
        self.password = password
        self.timeout = timeout
        self.method = method
        self.fast_open = fast_open

    def dump(self):
        return ''

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