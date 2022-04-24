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

    # Error check on interface path before constructing strings that have to be executed
    if interface_conf_path[-1] != "/":
        interface_path = interface_conf_path + "/"
        print("Pfad wurde korrigiert!")
        print("Neuer Pfad: " + interface_path)


    shutdown_string = "wg-quick down " + interface_name
    delete_string = " cd " + interface_conf_path + " && rm -rf " + interface_conf_name + " && rm -rf " + interface_pubkey_name + " && rm -rf " + interface_privkey_name + " && echo \"Interface wurde gelöscht!\""

    os.system(shutdown_string)
    os.system(delete_string)

    # Prompt if the current overview of interfaces should be printed
    print_overview = input("Soll die Übersicht der aktuellen Interfaces ausgegeben werden? [Y/N]: ")
    if print_overview in ("Y", "y"):
        os.system("wg show")
        input("Eine Taste drücken um fortzufahren: ")