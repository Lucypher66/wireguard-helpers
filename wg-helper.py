#!/bin/python3

import os
import authorize_peer_on_server
import deauthorize_peer_on_server
import add_server_interface
import add_peer_interface
import delete_interface
import uninstall

# Root check
if os.geteuid() != 0:
    exit("Root-Rechte werden benötigt! Bitte als root- oder sudo-user ausführen!")

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
    print("wg-helper wurde aktualisiert!")

if answer == "7":
    uninstall.uninstall()

if answer == "8":
    exit("wg-helper wird beendet.")