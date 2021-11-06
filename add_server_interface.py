#!/bin/python3
import os

def generate_interface_config():

    #Root check
    if os.geteuid() != 0:
        exit("Root-Rechte werden benötigt! Bitte als root- oder sudo-user ausführen!")

    #Gather interface variables
    interface_name = input("Name des neuen Interfaces angeben: ")
    interface_path = input("Wo soll die Konfigurationsdatei gespeichert werden? ")
    interface_address = input("Adresse des neuen Interfaces angeben: ")
    interface_subnetmask = input("Subnetzmaske des neuen Interfaces angeben (0-32): ")
    save_config_prompt = input("Konfiguration beim shutdown des Interfaces speichern? (empfohlen) [Y/N]: ")
    listen_port = input("Auf welchem Port soll WireGuard lauschen? (1025-65535): ")
    outgoing_interface = input("Lauschendes Interface angeben: ")

    # Error check on interface path before constructing strings that have to be executed
    if interface_path[-1] != "/":
        interface_path = interface_path + "/"
        print("Pfad wurde korrigiert!")
        print("Neuer Pfad: " + interface_path)

    #Prepare interface variables
    interface_conf_name = interface_name + ".conf"
    interface_conf_path = interface_path + interface_conf_name
    interface_ip_and_subnetmask = interface_address + "/" + interface_subnetmask
    interface_private_key_file_name = interface_name + "_private_key"
    interface_public_key_file_name = interface_name + "_public_key"
    interface_genkeys_string = "wg genkey | tee " + interface_private_key_file_name + " | wg pubkey > " + interface_public_key_file_name
    touch_conf_file_string = "touch " + interface_conf_path

    #Create interface file
    os.system(touch_conf_file_string)

    #Generate needed keys and print current working directory
    os.system("cd " + interface_path + " && pwd && " + interface_genkeys_string)

    with open(interface_path + interface_private_key_file_name, "r") as privkey:
        interface_private_key = privkey.read().rstrip()

    with open(interface_path + interface_public_key_file_name, "r") as pubkey:
        interface_public_key = pubkey.read().rstrip()




    #Prepare interface strings for input
    insert_interface_prefix = "echo \"[Interface]\" > " + interface_conf_path
    insert_interface_address = "echo \"Address = " + interface_ip_and_subnetmask + "\" >> " + interface_conf_path
    insert_save_config = "echo \"SaveConfig = True\" >> " + interface_conf_path
    insert_postup = "echo \"PostUp = iptables -A FORWARD -i " + interface_name + " -j ACCEPT; iptables -t nat -A POSTROUTING -o " + outgoing_interface + " -j MASQUERADE;\" >> " + interface_conf_path
    insert_postdown = "echo \"PostDown = iptables -D FORWARD -i " + interface_name + " -j ACCEPT; iptables -t nat -A POSTROUTING -o " + outgoing_interface + " -j MASQUERADE;\" >> " + interface_conf_path
    insert_listenport = "echo \"ListenPort = " + listen_port + "\" >> " + interface_conf_path
    insert_privatekey = "echo \"PrivateKey = " + interface_private_key + "\" >> " + interface_conf_path

    #Prepare empty line string for beauty purposes
    insert_empty_line = "echo \"\" >> " + interface_conf_path

    #Insert interface config
    os.system(insert_interface_prefix)
    os.system(insert_interface_address)
    if save_config_prompt == "Y" or save_config_prompt == "y":
        os.system(insert_save_config)
    os.system(insert_postup)
    os.system(insert_postdown)
    os.system(insert_listenport)
    os.system(insert_privatekey)
    os.system("cat " + interface_conf_path)

    #Insert empty line for beauty purposes
    os.system(insert_empty_line)

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