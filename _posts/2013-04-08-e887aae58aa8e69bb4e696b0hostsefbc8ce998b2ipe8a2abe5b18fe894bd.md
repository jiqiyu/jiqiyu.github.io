---
author: huxingyi
comments: true
date: 2013-04-08 12:29:52+00:00
layout: post
link: http://www.jiqiyu.com/?p=1200
slug: '%e8%87%aa%e5%8a%a8%e6%9b%b4%e6%96%b0hosts%ef%bc%8c%e9%98%b2ip%e8%a2%ab%e5%b1%8f%e8%94%bd'
title: 自动更新hosts，防ip被屏蔽
wordpress_id: 1200
categories:
- 杂
tags:
- gfw
- hosts
---

自动更新hosts，防ip被屏蔽，如果网络不通，会不断下载（间隔5秒左右），下载完成后，会对比hosts是否已修改（主要是为了使用SSD硬盘的考虑），如果已修改则更新到hosts。可以设为开机启动。
批处理文件在这里：
https://gist.github.com/huxingyi/5334553
