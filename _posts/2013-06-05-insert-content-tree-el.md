---
author: nanyu
comments: true
date: 2013-06-05 04:48:14+00:00
layout: post
link: http://www.jiqiyu.com/?p=1273
slug: insert-content-tree-el
title: insert-content-tree.el
wordpress_id: 1273
categories:
- 杂
tags:
- elisp
- emacs
- package
- plugin
- tree
---

根據給定的字符串生成一棵目錄樹（前後newline包裹），插到當前光標所在位置（emacs裡）的後面。接受的字符串格式跟`mkdir -p`批量建目錄時接受的串格式一樣，比如，


    
    <code>
    (insert-contents-tree "CONTENTS TITLE/{第一章/{1.1/{1.1.1/{1.1.1.1,1.1.1.2,1.1.1.3},1.1.2,1.1.3},1.2/{1.2.1,1.2.2},1.3},第二章/{2.1,2.2},第三章/{3.1,3.2}}")</code>



會插入:

    
    
    <code>
    CONTENTS TITLE
    |-- 第一章
    |   |-- 1.1
    |   |   |-- 1.1.1
    |   |   |   |-- 1.1.1.1
    |   |   |   |-- 1.1.1.2
    |   |   |   `-- 1.1.1.3
    |   |   |-- 1.1.2
    |   |   `-- 1.1.3
    |   |-- 1.2
    |   |   |-- 1.2.1
    |   |   `-- 1.2.2
    |   `-- 1.3
    |-- 第二章
    |   |-- 2.1
    |   `-- 2.2
    `-- 第三章
        |-- 3.1
        `-- 3.2
    </code>
    



[https://github.com/jiqiyu/insert-contents-tree.el/blob/master/insert-content-tree.el](https://github.com/jiqiyu/insert-contents-tree.el/blob/master/insert-content-tree.el)
