#!/bin/python3
import os

def add_peer():
    if os.geteuid() != 0:
        exit("Root-Rechte werden benötigt! Bitte als root- oder sudo-user ausführen!")

    interface = input("WireGuard-Interface angeben: ")
    pubkey = input("Public Key des Peers eingeben: ")
    peer_ip = input("IP-Adresse des Tunnel-Interfaces angeben: ")

    wireguard_command = "wg set " + interface + " peer " + pubkey + " allowed-ips " + peer_ip + "/32"

    os.system(wireguard_command)

add_peer()