#! /usr/bin/env python3
# Author: ISaleem
# Version: 1.0
# Description: This script will simulate a high street bank PIN machine
"""
   DocString  
"""
master_pin = "0123"
pin = None
attempt = 0

while pin != master_pin and attempt < 3:
    pin = input("Enter PIN: ")
    attempt +=1

    if pin == master_pin:
        print("Valid PIN")
        break
    else:
        print("Invalid PIN")


print("Done")