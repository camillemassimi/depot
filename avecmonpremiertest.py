#! /bin/env python3
# -*- coding: utf-8 -*-

import re

pattern = re.compile(r'^([0-9\.]+) [^[]+\[([^ ]*) .*(GET)|(HEAD) ([^ ]+) .+[-\d] "([^"]*)"') 

echecs=[]
with open("/users/2021ds/192001678/Documents/access.log",encoding="utf-8") as f : 
    for line in f : 
        found = pattern.search(line.strip())
        if found: 
            print(found.groups())
        else : 
            echecs += [ line ]

print(f"\nlignes en echecs de decoupages : \n{echecs}")