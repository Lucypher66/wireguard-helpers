import sys

def validate_command_line_arguments():
    if sys.argv[2] != "--interface-name":
        exit("Unknown argument: " + sys.argv[2])

    if sys.argv[4] != "--config-path":
        exit("Unknown argument: " + sys.argv[4])

    if sys.argv[6] != "--interface-address":
        exit("Unknown argument: " + sys.argv[6])

    if sys.argv[8] != "--interface-subnetmask":
        exit("Unknown argument: " + sys.argv[8])

    if sys.argv[10] != "--save-config":
        exit("Unknown argument: " + sys.argv[10])

    if sys.argv[12] != "--local-listen-port":
        exit("Unknown argument: " + sys.argv[12])

    if sys.argv[14] != "--peer-pubkey":
        exit("Unknown argument: " + sys.argv[14])

    if sys.argv[16] != "--tunnel-ips":
        exit("Unknown argument: " + sys.argv[16])

    if sys.argv[18] != "--tunnel-subnetmask":
        exit("Unknown argument: " + sys.argv[18])

    if sys.argv[20] != "--peer-ip-or-domain":
        exit("Unknown argument: " + sys.argv[20])

    if sys.argv[22] != "--peer-listen-port":
        exit("Unknown argument: " + sys.argv[22])

    if sys.argv[24] != "--set-keepalive":
        exit("Unknown argument: " + sys.argv[24])

    if sys.argv [26] != "--keepalive-seconds":
        exit("Unknown argument: " + sys.argv[26])