#!/bin/python3
import os

answer = input("Soll wg-helper installiert werden? [Y/N]: ")

if answer == "y" or answer == "Y":
    os.system("mkdir /etc/wg-helper")
    os.system("cp -r * /etc/wg-helper")
    os.system("ln -sf /etc/wg-helper/wg-helper.py /usr/bin/wg-helper")
    print("wg-helper wurde installiert und kann mit \"sudo wg-helper\" aufgerufen werden!")

else:
    exit("wg-helper wird nicht installiert.")