#!/bin/python3
import os

def delete_interface():

    #Root check
    if os.geteuid() != 0:
        exit("Root-Rechte werden benötigt! Bitte als root- oder sudo-user ausführen!")

    interface_name = input("Name des zu löschenden Interfaces angeben: ")
    interface_conf_path = input("Pfad in dem die Konfigurationsdatei liegt angeben: ")

    interface_conf_name = interface_name + ".conf"
    interface_pubkey_name = interface_name + "_public_key"
    interface_privkey_name = interface_name + "_private_key"

    delete_string = " cd " + interface_conf_path + " && rm -rf " + interface_conf_name + " && rm -rf " + interface_pubkey_name + " && rm -rf " + interface_privkey_name

    os.system(delete_string)