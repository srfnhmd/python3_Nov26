#! /usr/bin/env python3
# Author: ISaleem
# Version: 1.0
# Description: This script will demo HOWTO
"""
   DocString  
"""

for pos in range(0, 65536, 1):
    try:
        print(chr(pos), end=" ")
        if pos % 16 == 0:
            print()

    except UnicodeEncodeError:
        print(" ")