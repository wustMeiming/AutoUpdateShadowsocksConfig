#AutoUpdateShadowsocksConfig

###环境要求：
1. 安装shadowsocks（必须）
2. 代理插件（必须，用于浏览器，如chrome可以安装SwitchyOmega插件）
2. 安装proxychains（非必须，用于终端代理）


###1.ubuntu安装shadowsocks

用PIP安装很简单

```bash
apt-get install python-pip
```
接着安装shadowsocks
```bash
pip install shadowsocks
```
当然你在安装时候肯定有提示需要安装一些依赖比如python-setuptools m2crypto ，依照提示安装然后再安装就好。也可以网上搜索有很多教程的。

####2.启动shadowsocks

安装好后，在本地我们要用到sslocal ，终端输入sslocal --help 可以查看帮助

通过帮助提示我们知道各个参数怎么配置，比如 sslocal -c 后面加上我们的json配置文件，或者像下面这样直接命令参数写上运行。

比如 sslocal -s 11.22.33.44 -p 50003 -k "123456" -l 1080 -t 600 -m aes-256-cfb

-s表示服务IP,
-p指的是服务端的端口，
-l是本地端口默认是1080, 
-k 是密码（要加""）, 
-t超时默认300,
-m是加密方法默认aes-256-cfb，

为了方便我推荐直接用sslcoal -c 配置文件路径 这样的方式，简单好用。

我们可以在/home/meiming/ 下新建个文件 ss_conf.json  (meiming是我在我电脑上的用户名，这里路径你自己看你的)。内容是这样：

>{
>"server":"11.22.33.44",
>"server_port":50003,
>"local_port":1080,
>"password":"123456",
>"timeout":600,
>"method":"aes-256-cfb"
>}

server  你服务端的IP
servier_port  你服务端的端口
local_port  本地端口，一般默认1080
passwd  ss服务端设置的密码
timeout  超时设置 和服务端一样
method  加密方法 和服务端一样

确定上面的配置文件没有问题，然后我们就可以在终端输入
```bash
sslocal -c /home/meiming/ss_conf.json
```
回车运行。如果没有问题的话，下面会是这样.
>INFO: loading config from ss_conf.json
>2016-07-08 09:03:56 INFO     loading libcrypto from libcrypto.so.1.0.0
>2016-07-08 09:03:56 INFO     starting local at 127.0.0.1:1080

<strong style="color: rgb(255,0,0); font-size: large">我们的脚本的作用就是自动生成配置文件</strong>
###3. 如何使用我们的脚本

1. 首先下载脚本 
```bash
git clone https://git.oschina.net/meiming/AutoUpdateShadowsocksConfig.git
```
2. 修改配置文件存放路径
根据自己的喜好选择一个路径存放
打开 auto_config.py 文件，找到主函数位置，修改对应位置
```python
# 配置文件存放位置
configFile = "/home/meiming/ss_conf.json"
```
3. 小Tips
编写一个脚本 ss_start.sh，在需要使用的时候开一个终端运行即可 ./ss_start.sh
```bash
#运行下载的脚本，自动生成对应代理服务器配置文件
python /home/meiming/AutoUpdateShadowsocksConfig/auto_config.py
#利用脚本生成的配置文件，启动shadowsocks
sslocal -c /home/meiming/ss_conf.json
```
配置完之后就可以访问google了吗？ 
其实并不可以！ 
怎么办？ 
安装浏览器代理插件 
我们需要给chrome安装SwitchyOmega插件，但是没有代理之前是不能从谷歌商店安装这个插件的，但是我们可以从Github上直接下载最新版 https://github.com/FelisCatus/SwitchyOmega/releases/ （这个是chrome的）然后浏览器地址打开chrome://extensions/，将下载的插件托进去安装。 

SwitchyOmega的安装和配置，可以参考[Chrome 代理插件 SwitchyOmega 超详细图文教程](http://www.ihacksoft.com/chrome-switchyomega.html)
proxychains的安装和配置，可以参考[利用proxychains在终端使用socks5代理](http://www.tuicool.com/articles/rUNFF3)