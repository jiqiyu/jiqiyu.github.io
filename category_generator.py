#!/usr/bin/env python

'''
category_generator.py
Copyright 2017 Long Qian
Contact: lqian8@jhu.edu
This script creates categories for your Jekyll blog hosted by Github page.
No plugins required.

Modified by jiqiyu.com to recognize line splitted categories
25/12/2018
'''

import glob
import os

post_dir = '_posts/'
category_dir = 'category/'

filenames = glob.glob(post_dir + '*md')

total_categories = []
for filename in filenames:
    f = open(filename, 'r')
    crawl = False
    for line in f:
        current_categories = line.strip().split()
        if len(current_categories) >= 1:
            if current_categories[0] == 'categories:':
                crawl = True
            elif current_categories[0] == '-':
                if crawl:
                    total_categories.extend(current_categories[1:])
            else:
                crawl = False
    f.close()
total_categories = set(total_categories)

old_categories = glob.glob(category_dir + '*.md')
for category in old_categories:
    os.remove(category)

if not os.path.exists(category_dir):
    os.makedirs(category_dir)

for category in total_categories:
    category_filename = category_dir + category + '.md'
    f = open(category_filename, 'a')
    write_str = '---\nlayout: categorypage\ntitle: \"Category: ' + category + '\"\ncategory: ' + category + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()
print("categories generated, count", total_categories.__len__())
