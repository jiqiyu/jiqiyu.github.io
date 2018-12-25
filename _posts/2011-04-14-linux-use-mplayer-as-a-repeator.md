---
author: nanyu
comments: true
date: 2011-04-14 15:38:51+00:00
layout: post
link: http://www.jiqiyu.com/?p=792
slug: linux-use-mplayer-as-a-repeator
title: '[linux] Use mplayer as a repeator'
wordpress_id: 792
categories:
- 杂
tags:
- linux
- mplayer
- python
---


Sometimes we could encounter some large size media file, and we may want to split it into parts so that we can listen around, back and forth. Mplayer has an '-ss hh:mm:ss' option by which we can start listening from any point we want, so I just write a script for people to use mplayer as a repeator more convinience, without really break the media file into parts. The script is just a wrapper, outside mplayer. The good thing is, we can use mplayer's all function as we are using itself when we playing stuff, use this script.






Program: [repeator.py](http://jiqiyu.com/codes/repeator.html) 
Options:
    -h - displays this help message, expects no argument
    -p - displays default playlist, expects no argument
    --loop - sets loop to True, expects no argument
    --part - expects an number as argument
    --file - expects one argument which is the path to your audio file
    --playlist - explicitly specifies a playlist file, this option must use together
                   with --file option
    --clist - creates a playlist file, expects list name as its argument

