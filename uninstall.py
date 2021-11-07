#!/bin/python3
import os

def uninstall():
    answer = input("Soll wg-helper deinstalliert werden? [Y/N]: ")

    if answer == "y" or answer == "y":
    os.system("rm -rf /etc/wg-helper")
    os.system("rm /usr/bin/wg-helper")
    print("wg-helper wurde deinstalliert!")

    else:
    exit("Deinstallation abgebrochen")