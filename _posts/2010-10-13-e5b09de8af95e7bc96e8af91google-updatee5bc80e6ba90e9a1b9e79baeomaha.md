---
author: huxingyi
comments: true
date: 2010-10-13 08:07:43+00:00
layout: post
link: http://www.jiqiyu.com/?p=578
slug: '%e5%b0%9d%e8%af%95%e7%bc%96%e8%af%91google-update%e5%bc%80%e6%ba%90%e9%a1%b9%e7%9b%aeomaha'
title: 尝试编译google update开源项目:omaha
wordpress_id: 578
categories:
- 杂
tags:
- omaha
---

按照http://code.google.com/p/omaha/wiki/DeveloperSetupGuide的说明安装好环境后,尝试Build,报错:
EnvironmentError: No module named _scons_optparse:
在报上面的错误后,我下载了 http://optik.sourceforge.net/ 并安装了.不过,我觉得应该不装这个也行.因为我装了这个以后,还是报上面的错误.
从http://www.scons.org/doc/1.3.0.d20100606/HTML/scons-api/SCons.compat._scons_optparse-pysrc.html下载源码,在EDITPLUS中用正则"^[ ]*[0-9]+ [ -]"替换前面的行号和空格.并保存到C:Python26Libsite-packagesscons-2.0.1SConscompat中并命名为:_scons_optparse.py
现在原来的错误没有了,报出新错:By convention, the build number in VERSION (currently 187) should be odd.
其实187已经是奇数了,估计是我下载的scons版本不同.注释掉if 2 * (original_value / 2) == original_value:和后面的两行就可以开始编译了.
编译一段时间后会报错,原因似乎是因为"omahathird_partygeckoincludenpruntime.h"这个文件含非936的字符.将此文件改为UTF-8重新编译.
最后,仍然报错:
Successfully signed and timestamped: scons-outdbg-winobjinstallersGoogleUpda
teSetup.exe
Install file: "scons-outdbg-winobjinstallersGoogleUpdateSetup.exe" as "scons
-outdbg-winclickonce_deploymentbinGoogleUpdateSetup.exe"
Internal error, please try again. ??????????"Microsoft.Build.Tasks.v3.5, Version
=3.5.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"??????????The system
cannot find the file specified.
scons: *** [scons-outdbg-winobjclickonceclickonce_bootstrap.exe.manifest] Er
ror 2
scons: building terminated because of errors.
似乎已经编译出安装程序了,在"omahascons-outdbg-winclickonce_deploymentbin"下也可以看到已经生成了GoogleUpdateSetup.exe,但是双击运行会报错.
上面说的Internal error, please try again.不知道是什么错误,我已经不想再try again了.
放弃omaha.
