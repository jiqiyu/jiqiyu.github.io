---
author: nanyu
comments: true
date: 2010-09-18 03:36:05+00:00
layout: post
link: http://www.jiqiyu.com/?p=527
slug: always-forget-but-sometimes-useful-ssh-tip
title: Always Forget but Sometimes Useful - SSH Tip
wordpress_id: 527
categories:
- 杂
tags:
- SSH
- tips
---

This article is granted to use as you want, it is also not necessary to specify "source from jiqiyu.com" . The contents of the article is collected from the Internet,  you can find it elsewhere, anywhere. However, this article contains the following topics:





1. Connect to ssh without inputting password everytime   
2. Fix ssh timeout


<!-- more -->
  

**_Connect to ssh without inputting password everytime_**



The first step is to create a public key to make a secure authentication to the server. Launch a shell terminal on your linux desktop and run the following command:





<blockquote># ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/user/.ssh/id_rsa.
Your public key has been saved in /home/user/.ssh/id_rsa.pub.</blockquote>





This step generates the public key and stores it into the file /home/user/.ssh/id_rsa.pub. When asked which file you want the key to be written to, just hit Enter to pick the suggested option. Similarly, when prompted for a passphrase just hit the Enter key twice. This file is stored in your home directory, in the .ssh folder which holds all the SSH server’s configuration files. So, next, you need to copy this file to the server to which you want to be able to SSH without a password.





<blockquote># scp ~/.ssh/id_rsa.pub username@remoteserver.com:/home/username/</blockquote>





Replace both instances of username in the above command with the username you use to log on to your remote server, and remoteserver.com with the host name or IP address of remote server. Now SSH into that server and add your desktop’s public key to the server’s SSH configuration:





<blockquote># ssh username@remoteserver.com
# cat ~/id_rsa.pub >> ~/.ssh/authorized_keys</blockquote>





Then you need to set the permission of the file ~/.ssh/authorized_keys correctly:





<blockquote># chmod 644 ~/.ssh/authorized_keys</blockquote>





Done here.



**_Fix ssh timeout_**



If your ssh session times out frequently, the following methods would help. 





Solution 1: On the server, login as root and edit /etc/ssh/sshd_config and add the line





<blockquote>ClientAliveInterval 60</blockquote>





Solution 2: As root on your desktop (or client) machine, edit /etc/ssh/ssh_config and add the line





<blockquote>ServerAliveInterval 60</blockquote>





Solution 3: Login as root and open /etc/ssh/sshd_config,  edit(or add) the line contains "ServerAliveInterval", make it a big number, like 3600 or 7200(an hour or two), this mean you leave the timeout control to the firewall. Take iptables for example, it takes the system defalt tcp keepalive settings, use these commands to check it out





<blockquote># cat /proc/sys/net/ipv4/tcp_keepalive_time
7200

# cat /proc/sys/net/ipv4/tcp_keepalive_intvl
75

# cat /proc/sys/net/ipv4/tcp_keepalive_probes
9</blockquote>





The first two parameters are expressed in seconds, and the last is the pure number. This means that the keepalive routines wait for two hours (7200 secs) before sending the first keepalive probe, and then resend it every 75 seconds. If no ACK response is received for nine consecutive times, the connection is marked as broken. Suppose you decide to configure the host so that keepalive starts after ten minutes of channel inactivity, and then send probes in intervals of one minute. Because of the high instability of our network trunk and the low value of the interval, suppose you also want to increase the number of probes to 20.





Here's how we would change the settings:





<blockquote># echo 600 > /proc/sys/net/ipv4/tcp_keepalive_time

# echo 60 > /proc/sys/net/ipv4/tcp_keepalive_intvl

# echo 20 > /proc/sys/net/ipv4/tcp_keepalive_probes</blockquote>





Well, this is it.
