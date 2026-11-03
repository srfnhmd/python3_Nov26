#! /usr/bin/env python3
# Author: ISaleem
# Version: 1.0
# Description: This script will demo HOWTO
"""
   DocString  
"""

line = "root:x:0:0:The Super User:/root:/bin/ksh"

fields = line.split(":")
fields[4] = "The Admin"
fields[6] = "/bin/bash"

line = ":".join(fields)
print("Modified line =", line)