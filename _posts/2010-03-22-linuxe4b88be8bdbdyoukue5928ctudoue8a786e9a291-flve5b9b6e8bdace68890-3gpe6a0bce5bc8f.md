---
author: nanyu
comments: true
date: 2010-03-22 09:14:11+00:00
layout: post
link: http://www.jiqiyu.com/?p=303
slug: linux%e4%b8%8b%e8%bd%bdyouku%e5%92%8ctudou%e8%a7%86%e9%a2%91-flv%e5%b9%b6%e8%bd%ac%e6%88%90-3gp%e6%a0%bc%e5%bc%8f
title: '[linux]下载youku和tudou视频(.flv)并转成.3gp格式'
wordpress_id: 303
categories:
- Digital Life
tags:
- 3gp
- flv
- tudou
- youku
- 下载
- 手机
---

如果想要把youku和tudou上喜欢的视频放在手机上看要怎么办呢？在linux下要下载youku和tudou视频非常简单，只要打开想要下载的youku或tudou的视频所在的那个页面，当看到页面中的播放器的下载进度条满格后，如图

![screenshot](http://www.piguban.com/wp-content/uploads/2010/03/screenshot.png)

在Terminal中输入：


<blockquote>ls /tmp | grep Flash</blockquote>


我们会看到当前网页中播放的这个视频已经存在/tmp文件夹中了，例如我这里列出的是FlashnY5hnQ，只要复制出来并重命名就可以了，这里假设我们命名为file.flv, 具体操作是在Terminal中输入：


<blockquote>cp /tmp/FlashnY5hnQ file.flv</blockquote>


这样视频就保存在电脑上当前文件来里了，但是我们知道手机上支持的格式是3gp，所以我们还要把flv转换成3gp，用强大的ffmpeg几乎转成什么格式都可以，在Terminal中输入:


<blockquote>ffmpeg -y -i file.flv -s 176x144 -b 200k -vcodec h263 -acodec libopencore_amrnb -ac 1 -ar 8000 -r 25 -ab 12200 outputfile.3gp</blockquote>


转换成功后，把视频(outputfile.3gp)考到手机上就可以在手机上看了:D
