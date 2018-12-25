---
author: huxingyi
comments: true
date: 2012-09-28 14:24:38+00:00
layout: post
link: http://www.jiqiyu.com/?p=1101
slug: centos%e4%b8%8byum%e5%ae%89%e8%a3%85%e9%85%8d%e7%bd%aesamba
title: centOS下yum安装配置samba
wordpress_id: 1101
categories:
- Digital Life
tags:
- samba
- yum
---

centOS下yum安装配置samba
http://lxsym.blog.51cto.com/1364623/289156

#yum -y install samba

#whereis samba

#vi /etc/samba/smb.conf
在最后添加：
[share]
comment = MyCentOS
path = /home/hxyman
guest ok = yes
writeable = yes
（建立linux共享目录 [http://renren4.iteye.com/blog/492156]）

#/sbin/service smb restart

#/sbin/chkconfig --level 5 smb on  （开机即开启共享）

#/sbin/chkconfig --level 5 smb off   (关闭开机共享)

#smbpasswd -a hxyman (设密码)
提示要求输入密码：New SMB password:
(Linux建立samba共享服务给Windows使用 [http://www.51testing.com/html/88/n-218388.html])
