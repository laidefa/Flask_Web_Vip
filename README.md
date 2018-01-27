# Flask_Web_Vip
Flask优酷、爱奇艺、腾讯VIP破解

------------------------------------------------------------------------------------------------------------------------------------------
# 效果展示

![优酷、爱奇艺、腾讯VIP视频免费观看](https://github.com/laidefa/Flask_Web_Vip/raw/master/web_vip/static/web.png)


----------------------------------------------------------------------------------------------------------------------------------------
# 主要技术
Python Flask框架开发网站-果汁大云播

优酷、爱奇艺、腾讯VIP视频免费观看


----------------------------------------------------------------------------------------------------------------------------------------
# 网站地址
网站已部署阿里云服务器

访问此链接可打开：http://101.37.147.236:1518/

----------------------------------------------------------------------------------------------------------------------------------------
# 如何运行
编写 start_web_vip.sh 脚本

``` 
#!/bin/bash
python /root/web_vip/hello.py
```

后台启动运行服务

### 方法1：

``` 
nohup ./start_web_vip.sh >>myjob.txt &
```

### 方法2：使用supervisor保持python进程运行

linux 下 执行以下命令运行
``` 
sudo supervisord 
```

--------------------------------------------------------------------------------------------------------------------------------------
# Supervisord安装配置

Supervisord是一个守护进程的工具，当进程意外终止或服务器掉电起来后，希望进程能够自动运行，supervisord可以很好的为我们做这件事情。同时supervisord也

自带监控界面，可以通过浏览器灵活的查看、操作。

### 1、supervisor 安装

- ubuntu:sudo apt-get install supervisor 

- centos: yum install supervisor

- pip:pip install supervisor


### 2.配置supervisord.conf文件


首先创建配置文件：

- echo_supervisord_conf > /etc/supervisord.conf


然后找到supervisord.conf配置文件，一般centos 在/etc/ 目录下，ubuntu 在/etc/supervisor/ 目录下，用root权限打开该文件：

- sudo vim /etc/supervisord.conf

- sudo vim /etc/supervisor/supervisord.conf


在文件末尾添加如下几行：


``` 
[program:web_vip]
command=python /root/web_vip/hello.py
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/root/code/myjob.log
startsecs=1 
startretries=3

```


注释：

- 第一行的myProgram自己取个名字，表示你的项目就行 

- 第二行的python /root/web_vip/hello.py表示你运行程序的命令 

- 第三行表示自动启动，如果值为false则表示不自动启动 

- 第四行表示自动重启，如果值为false则表示不自动重启 

- 第五行表示如果为true，则stderr的日志会被写入stdout日志文件中默认为false，非必须设置

- 第六行表示程序打印出的信息都记录在该myjob.log文件内，是log文件

- 第七行表示这个选项是子进程启动多少秒之后，此时状态如果是running，则我们认为启动成功了

- 第八行表示当进程启动失败后，最大尝试启动的次数，当超过3次后，supervisor将把此进程的状态置为FAIL


### 3、supervisor 常用命令


``` 
sudo service supervisor stop #停止supervisor服务

sudo service supervisor start #启动supervisor服务

supervisorctl shutdown #关闭所有任务

supervisorctl stop|start program_name #启动或停止服务

supervisorctl status #查看所有任务状态
```

### supervisor 官方网站

- https://github.com/Supervisor/supervisor
- http://supervisord.org/


----------------------------------------------------------------------------------------------------------------------------------------
# 联系我

微信：laidefa

CSDN博客： http://blog.csdn.net/u013421629?viewmode=contents

-----------------------------------------------------------------------------------------------------------------------------------------
