---
author: nanyu
comments: true
date: 2010-10-23 02:35:49+00:00
layout: post
link: http://www.jiqiyu.com/?p=583
slug: centos-security
title: CentOS Security
wordpress_id: 583
categories:
- 杂
tags:
- server
---

As I've subscribed to a new VPS recently, I then configured the server again. Fortunately, there's plenty of resources over the Internet, for further use, I write them down.



	
  1. Hardening CentOS

[http://wiki.centos.org/HowTos/OS_Protection](http://wiki.centos.org/HowTos/OS_Protection)
	
  2. Securing SSH

[http://wiki.centos.org/HowTos/Network/SecuringSSH](http://wiki.centos.org/HowTos/Network/SecuringSSH)
	
  3. Clear Shell History on Your Screen When You Logout

[http://www.cyberciti.biz/tips/howto-clear-screen-when-you-logout.html](http://www.cyberciti.biz/tips/howto-clear-screen-when-you-logout.html)(If this article can't answer your question, the comments probably could)
	
  4. IPTables

[http://wiki.centos.org/HowTos/Network/IPTables](http://wiki.centos.org/HowTos/Network/IPTables)
If there's other services on your server, like vpn,ftp,etc., you should configure the iptables to allow them, since you set DROP as your default policy.
The above are the most basic.
