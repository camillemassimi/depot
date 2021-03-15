#! /bin/env python3
# -*- coding: utf-8 -*-

import re

pattern = re.compile(r'^(\S+).+\[(\S+) .*"(?:GET|POST) (.*?) HTTP.*?".*?"(.*?)"')

echecs = []
with open("accesslog", encoding="utf-8") as f:
  for line in f:
    found = pattern.search(line.strip())
    if found:
      print(found.groups())
    else:
      echecs += [line]

print("\nlignes en échec de découpage : ", end="")
input("(press a key...)")
print(echecs)

