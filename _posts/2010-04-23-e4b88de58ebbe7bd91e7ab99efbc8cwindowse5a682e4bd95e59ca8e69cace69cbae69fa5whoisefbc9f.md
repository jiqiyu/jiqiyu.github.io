---
author: huxingyi
comments: true
date: 2010-04-23 01:40:22+00:00
layout: post
link: http://www.jiqiyu.com/?p=331
slug: '%e4%b8%8d%e5%8e%bb%e7%bd%91%e7%ab%99%ef%bc%8cwindows%e5%a6%82%e4%bd%95%e5%9c%a8%e6%9c%ac%e6%9c%ba%e6%9f%a5whois%ef%bc%9f'
title: 不去网站，windows如何在本机查whois？
wordpress_id: 331
categories:
- 杂
tags:
- 沒有標籤
---

#!-*- coding: cp936 -*-"
import socket
IP = 'whois.crsnic.net'
PORT = 43
while True:
	url = raw_input()
	if 'q' == url.rstrip():
		break
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print '.'
	s.connect((IP, PORT))
	print '.'
	s.send('%srn'%(url))
	print '.'
	while True:
		data = s.recv(1024)
		if not data: break
		print data
	s.close()
