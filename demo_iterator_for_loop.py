#! /usr/bin/env python3
# Author: ISaleem
# Version: 1.0
# Description: This script will demo HOWTO
"""
   DocString  
"""
import sys

idx = 0
heroes = ['abdul kalam', 'batman','super man','Goku','Vegeta']

for name in heroes:
    print(name, end="\n")
    heroes[idx] = name.upper()
    idx += 1
print("Heroes=", heroes)

for (idx,name) in enumerate(heroes):
    print(name.title(), end="\n")
    heroes[idx] = name.title()
print("Heroes=", heroes)

sys.exit(1)
