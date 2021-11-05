#!/bin/python3
import os

def remove_peer():
    if os.geteuid() != 0:
        exit("Root-Rechte werden benötigt! Bitte als root- oder sudo-user ausführen!")

    interface = input("WireGuard-Interface angeben: ")
    pubkey = input("Public Key des Peers eingeben: ")

    wireguard_command = "wg set " + interface + " peer " + pubkey + " remove"

    os.system(wireguard_command)

remove_peer()