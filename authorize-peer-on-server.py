#!/bin/python3
import os

def add_peer():

    #Root check
    if os.geteuid() != 0:
        exit("Root-Rechte werden benötigt! Bitte als root- oder sudo-user ausführen!")

    #Gather interface where the peer will be added to
    interface = input("WireGuard-Interface angeben: ")

    #Gather public key of the peer that will be authorized
    pubkey = input("Public Key des Peers eingeben: ")

    #Gather IP of peer that will be authorized
    peer_ip = input("IP-Adresse des Tunnel-Interfaces angeben: ")

    #Assemble wireguard command
    wireguard_command = "wg set " + interface + " peer " + pubkey + " allowed-ips " + peer_ip + "/32"

    #Execute wireguard command
    os.system(wireguard_command)

add_peer()