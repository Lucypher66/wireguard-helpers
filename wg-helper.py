#!/bin/python3

import authorize_peer_on_server
import deauthorize_peer_on_server
import add_server_interface
import add_peer_interface
import delete_interface
import uninstall

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
print("6. wg-helper deinstallieren")
print("7. Programm beenden")
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
    uninstall.uninstall()

if answer == "7":
    exit("wg-helper wird beendet.")