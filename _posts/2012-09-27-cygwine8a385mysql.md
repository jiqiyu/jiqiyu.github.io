---
author: huxingyi
comments: true
date: 2012-09-27 17:28:41+00:00
layout: post
link: http://www.jiqiyu.com/?p=1098
slug: cygwin%e8%a3%85mysql
title: Cygwin装Mysql
wordpress_id: 1098
categories:
- 杂
tags:
- cygwin
- mysql
---

按照这篇文章说的过程安装，中途有些微不同：
cygwin 安装 mysql
http://my.oschina.net/u/435872/blog/62324

$wget http://mirrors.ircam.fr/pub/mysql/Downloads/MySQL-5.1/mysql-5.1.65.tar.gz

$tar -xf mysql-5.1.65.tar.gz

$cd mysql-5.1.65

$./configure
提示出错了：
... ...
checking for termcap functions library... configure: error: No
curses/termcap library found

源码安装MYSQL提示NO CURSES/TERMCAP LIBRARY FOUND
http://www.sunnyu.com/?p=210

$cd ../

$wget http://ftp.gnu.org/pub/gnu/ncurses/ncurses-5.6.tar.gz

$tar zxvf ncurses-5.6.tar.gz

$cd ncurses-5.6

$./configure -prefix=/usr -with-shared -without-debug

$make

$make install clean

重新回来装mysql

$cd ../mysql-5.1.65

$./configure

出错：
In file included from readline.c:54:
readline/readline.h:79:29: sys/ttydefaults.h: No such file or directory

打开mysql-5.1.65/cmd-line-utils/libedit/readline/readline.h
注释掉第79行的#include 
（http://my.oschina.net/u/435872/blog/62324）

$make

再次出错：
In file included from el.h:50,
                 from vi.c:51:
chartype.h:65:2: warning: #warning Build environment does not support non-BMP ch
aracters
vi.c:921: error: syntax error before "char"
vi.c:922:36: macro "__weak_reference" requires 2 arguments, but only 1 given

#if defined(__weak_reference) && !defined(__FreeBSD__)
前面加上
#ifdef __CYGWIN__
#undef __weak_reference
#endif
（http://my.oschina.net/u/435872/blog/62324）

又出错了：
instance.cc: In function `int wait_process(My_process_info*)':
instance.cc:86: error: call of overloaded `wait(NULL)' is ambiguous
/usr/include/sys/wait.h:37: note: candidates are: pid_t wait(int*)
/usr/include/sys/wait.h:83: note:                 pid_t wait(wait*)
instance.cc:88: error: call of overloaded `waitpid(int&, NULL, int)' is ambiguou
s
/usr/include/sys/wait.h:38: note: candidates are: pid_t waitpid(pid_t, int*, int
)
/usr/include/sys/wait.h:85: note:                 pid_t waitpid(pid_t, wait*, in
t)
Makefile:820: recipe for target `mysqlmanager-instance.o' failed

修改：
mysql-5.1.65/server-tools/instance-manager/instance.cc:
把原来的：
  if (Manager::is_linux_threads())
    wait(NULL);                               /* LinuxThreads were detected */
  else
    waitpid(*pi, NULL, 0);
改为：
  if (Manager::is_linux_threads())
    wait((int *)NULL);                               /* LinuxThreads
were detected */
  else
    waitpid(*pi, (int *)NULL, 0);
(Re: Bug in sys/wait.h with
C++[http://cygwin.com/ml/cygwin/2012-02/msg00180.html])

$make

$make install
