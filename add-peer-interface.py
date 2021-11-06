#!/bin/python3
import os

#Root check
def remove_peer():
    if os.geteuid() != 0:
        exit("Root-Rechte werden benötigt! Bitte als root- oder sudo-user ausführen!")

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

def generate_interface_config():
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
    insert_interface_prefix = "echo \"[Interface]\" > " + interface_conf_path
    insert_interface_address = "echo \"Address = " + interface_ip_and_subnetmask + "\" >> " + interface_conf_path
    insert_save_config = "echo \"SaveConfig = True\" >> " + interface_conf_path
    insert_listenport = "echo \"ListenPort = " + local_listen_port + "\" >> " + interface_conf_path
    insert_privatekey = "echo \"PrivateKey = " + interface_private_key + "\" >> " + interface_conf_path

    #Prepare empty line string for beauty purposes
    insert_empty_line = "echo \"\" >> " + interface_conf_path

    #Prepare peer strings for input
    insert_peer_prefix = "echo \"[Peer]\" >> " + interface_conf_path
    insert_peer_public_key = "echo \"PublicKey = " + peer_pubkey + "\" >> " + interface_conf_path
    insert_tunnel_ips = "echo \"AllowedIPs = " + tunnel_ips + "/" + tunnel_subnet + "\" >>" + interface_conf_path
    insert_peer_ip_and_port = "echo \"Endpoint = " + peer_ip_or_domain + ":" + peer_listen_port + "\" >> " + interface_conf_path
    if set_keepalive == "y" or set_keepalive == "Y":
        insert_peer_keepalive = "echo \"PersistentKeepalive = " + keepalive_seconds + "\" >> " + interface_conf_path




    #Insert interface config
    os.system(insert_interface_prefix)
    os.system(insert_interface_address)
    if save_config_prompt == "Y" or save_config_prompt == "y":
        os.system(insert_save_config)
    os.system(insert_listenport)
    os.system(insert_privatekey)

    #Insert empty line for beauty purposes
    os.system(insert_empty_line)

    #Insert peer config
    os.system(insert_peer_prefix)
    os.system(insert_peer_public_key)
    os.system(insert_tunnel_ips)
    os.system(insert_peer_ip_and_port)
    if set_keepalive == "y" or set_keepalive == "Y":
        os.system(insert_peer_keepalive)
    os.system("cat " + interface_conf_path)

    #Insert empty line for beauty purposes
    os.system(insert_empty_line)

    #Prompt if the current overview of interfaces should be printed
    print_overview = input("Soll die Übersicht der aktuellen Interfaces ausgegeben werden? [Y/N]: ")
    if print_overview == "Y" or print_overview == "y":
        os.system("wg show")

    # Insert empty line for beauty purposes
    os.system(insert_empty_line)

    #Prompt if the newly created interface should be activated
    print_overview = input("Soll das neue Interface aktiviert werden? [Y/N]: ")
    if print_overview == "Y" or print_overview == "y":
        os.system("wg-quick up " + interface_name)

    # Insert empty line for beauty purposes
    os.system(insert_empty_line)

generate_interface_config()