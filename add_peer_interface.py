#!/bin/python3
import os
import sys

def generate_interface_config():

    #Root check
    if os.geteuid() != 0:
        sys.exit("Root-Rechte werden benötigt! Bitte als root- oder sudo-user ausführen!")

    #Gather interface variables
    interface_name = input("Name des neuen Interfaces angeben: ")
    interface_path = input("Wo soll die Konfigurationsdatei gespeichert werden? ")
    interface_address = input("Adresse des neuen Interfaces angeben: ")
    interface_subnetmask = input("Subnetzmaske des neuen Interfaces angeben (0-32): ")
    save_config_prompt = input("Konfiguration beim deaktivieren des Interfaces speichern? (empfohlen) [Y/N]: ")
    local_listen_port = input("Auf welchem Port soll WireGuard lauschen? (1025-65535) ")

    #Gather peer variables
    peer_pubkey = input("Wie lautet der Public Key des Peers? ")
    tunnel_ips = input("Welcher IP-Bereich soll durch den Tunnel geroutet werden? ")
    tunnel_subnet = input("Wie groß ist das Subnetz des IP-Bereichs, der durch den Tunnel geroutet wird? (0-32): ")
    peer_ip_or_domain = input("Wie lautet die IP-Adresse oder Domain des Peers? ")
    peer_listen_port = input("Auf welchem Port lauscht der Peer? ")
    set_keepalive = input("Soll der Tunnel konstant aufrecht erhalten werden? (empfohlen) [Y/N]: ")
    if set_keepalive == "y" or set_keepalive == "Y":
        keepalive_seconds = input("In welchem Zeitabstand (Sekunden) soll ein KeepAlive-Paket geschickt werden? ")

    # Error check on interface path before constructing strings that have to be executed
    if interface_path[-1] != "/":
        interface_path = interface_path + "/"
        print("Pfad wurde korrigiert!")
        print("Neuer Pfad: " + interface_path)

    #Prepare interface variables, will be refactored
    interface_conf_name = interface_name + ".conf"
    interface_conf_path = interface_path + interface_conf_name
    interface_ip_and_subnetmask = interface_address + "/" + interface_subnetmask
    interface_private_key_file_name = interface_name + "_private_key"
    interface_public_key_file_name = interface_name + "_public_key"
    interface_genkeys_string = "wg genkey | tee " + interface_private_key_file_name + " | wg pubkey > " + interface_public_key_file_name
    touch_conf_file_string = "touch " + interface_conf_path

    os.system(touch_conf_file_string)
    os.system("cd " + interface_path + " && pwd && " + interface_genkeys_string)

    with open(interface_path + interface_private_key_file_name, "r") as privkey:
        interface_private_key = privkey.read().rstrip()

    with open(interface_path + interface_public_key_file_name, "r") as pubkey:
        interface_public_key = pubkey.read().rstrip()

    #Prepare interface strings for input
    insert_interface_prefix = "[Interface]" + "\n"
    insert_interface_address = "Address = " + interface_ip_and_subnetmask + "\n"
    insert_save_config = "SaveConfig = True" + "\n"
    insert_listenport = "ListenPort = " + local_listen_port + "\n"
    insert_privatekey = "PrivateKey = " + interface_private_key + "\n"

    #Prepare empty line string for beauty purposes
    insert_empty_line = ""

    #Prepare peer strings for input
    insert_peer_prefix = "[Peer]" + "\n"
    insert_peer_public_key = "PublicKey = " + peer_pubkey + "\n"
    insert_tunnel_ips = "AllowedIPs = " + tunnel_ips + "/" + tunnel_subnet + "\n"
    insert_peer_ip_and_port = "Endpoint = " + peer_ip_or_domain + ":" + peer_listen_port + "\n"
    if set_keepalive == "y" or set_keepalive == "Y":
        insert_peer_keepalive = "PersistentKeepalive = " + keepalive_seconds  + "\n"

    #Insert interface config
    with open (interface_conf_path,"w") as conf_file:
        conf_file.write(insert_interface_prefix)
        conf_file.write(insert_interface_address)
        if save_config_prompt == "Y" or save_config_prompt == "y":
            conf_file.write(insert_save_config)
        conf_file.write(insert_listenport)
        conf_file.write(insert_privatekey)

        #Insert empty line for beauty purposes
        conf_file.write(insert_empty_line)

        #Insert peer config
        conf_file.write(insert_peer_prefix)
        conf_file.write(insert_peer_public_key)
        conf_file.write(insert_tunnel_ips)
        conf_file.write(insert_peer_ip_and_port)
        if set_keepalive == "y" or set_keepalive == "Y":
            conf_file.write(insert_peer_keepalive)
        conf_file.close()

    #Print empty line for beauty purposes
    print("")

    #Prompt if the public key should be printed
    print_overview = input("Soll der public key für das neu angelegte Interface ausgegeben werden? [Y/N]: ")
    if print_overview == "Y" or print_overview == "y":
        print(interface_public_key)

    #Insert empty line for beauty purposes
    os.system(insert_empty_line)

    #Prompt if the newly created interface should be activated
    print_overview = input("Soll das neue Interface aktiviert werden? [Y/N]: ")
    if print_overview == "Y" or print_overview == "y":
        os.system("wg-quick up " + interface_name)

    #Insert empty line for beauty purposes
    os.system(insert_empty_line)

    #Prompt if the current overview of interfaces should be printed
    print_overview = input("Soll die Übersicht der aktuellen Interfaces ausgegeben werden? [Y/N]: ")
    if print_overview == "Y" or print_overview == "y":
        os.system("wg show")
        input("Eine Taste drücken um fortzufahren: ")