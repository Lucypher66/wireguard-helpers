#!/bin/python3
import os
import sys

def remove_peer():

    #Root check
    if os.geteuid() != 0:
        sys.exit("Root-Rechte werden benötigt! Bitte als root- oder sudo-user ausführen!")

    #Gather interface name
    interface = input("WireGuard-Interface angeben: ")

    #Gather the pubkey of the peer that will be removed
    pubkey = input("Public Key des Peers eingeben: ")

    #Assemble wireguard command
    wireguard_command = "wg set " + interface + " peer " + pubkey + " remove"

    #Execute wireguard command
    os.system(wireguard_command)