---
author: huxingyi
comments: true
date: 2012-09-28 14:25:26+00:00
layout: post
link: http://www.jiqiyu.com/?p=1103
slug: error-while-loading-shared-libraries-libmysqlclient-so-16
title: 'error while loading shared libraries: libmysqlclient.so.16'
wordpress_id: 1103
categories:
- 杂
tags:
- 沒有標籤
---

error while loading shared libraries: libmysqlclient.so.16

这个方法不管用：
ln -s /usr/local/mysql/lib/libmysqlclient.so.16 /usr/lib/libmysqlclient.so.16
(读不到mysql库文件的故障排除 [http://www.linux521.com/2009/system/200909/8513.html])

这个办法仍然不管用
vi? /etc/ld.so.conf
添加
/usr/local/mysql/bin/mysql
(sphinx执行indexer 时报 libmysqlclient.so.16 错误，解决方法!
[http://blog.hucde.com/2010/06/10/88])

下面这个办法解决问题：
export LD_LIBRARY_PATH="/usr/local/lib/mysql:$LD_LIBRARY_PATH"
(编译php5.3.6出现问题cannot open shared object file
[http://hilinux.com/bbs/thread-2713-1-1.html])
