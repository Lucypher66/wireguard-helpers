#!/bin/python3

import os
import sys
import authorize_peer_on_server
import deauthorize_peer_on_server
import add_server_interface
import add_peer_interface
import delete_interface
import uninstall

# Root check
if os.geteuid() != 0:
    exit("Root-Rechte werden benötigt! Bitte als root- oder sudo-user ausführen!")

if sys.argv[1] == "--add-peer-interface":
    add_peer_interface.generate_interface_config(sys.argv[3], sys.argv[5], sys.argv[7], \
                                                 sys.argv[9], sys.argv[11], sys.argv[13], \
                                                 sys.argv[15], sys.argv[17], sys.argv[19], \
                                                 sys.argv[21],sys.argv[23],sys.argv[25],\
                                                 sys.argv[27])

if sys.argv[1] == "--create-server":
    add_server_interface.generate_interface_config(sys.argv[3], sys.argv[5], sys.argv[7], \
                                                 sys.argv[9], sys.argv[11], sys.argv[13], \
                                                 sys.argv[15],)

if sys.argv[1] == "--authorize-peer":
    pass

if sys.argv[1] == "--deauthorize-peer":
    pass

if sys.argv[1] == "--delete-interface":
    pass

run = True

def menu():

    print("################################################")
    print("#                                              #")
    print("#                  wg-helper                   #")
    print("#           Making WireGuard simple!           #")
    print("#                                              #")
    print("################################################")
    print("")
    print("1. Neuen Server anlegen")
    print("2. Neuen Peer hinzufügen")
    print("3. Peer autorisieren")
    print("4. Peer deautoriseren")
    print("5. Tunnel-Interface löschen")
    print("6. wg-helper aktualisieren")
    print("7. wg-helper deinstallieren")
    print("8. Programm beenden")
    print("")
    answer = input("Auswahl: ")

    if answer == "1":
        add_server_interface.generate_interface_config()

    if answer == "2":
        add_peer_interface.generate_interface_config()

    if answer == "3":
        authorize_peer_on_server.add_peer()

    if answer == "4":
        deauthorize_peer_on_server.remove_peer()

    if answer == "5":
        delete_interface.delete_interface()

    if answer == "6":
        os.system("cd /etc/wg-helper/")
        os.system("git pull")
        print("wg-helper ist auf dem aktuellsten Stand!")

    if answer == "7":
        uninstall.uninstall()

    if answer == "8":
        exit("wg-helper wird beendet.")



while run == True:
    os.system("clear")
    menu()