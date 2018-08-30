# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 11:29:19 2018

@author: dell
"""

bufsize = 100000
with open("sample.txt") as infile: 
    while True:
        lines = infile.readlines(bufsize)
        if not lines:
            break
        for line in lines:
            process(line) #do anything line by line