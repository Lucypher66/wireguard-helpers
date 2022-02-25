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

    if sys.argv[12] != "--listen-port":
        exit("Unknown argument: " + sys.argv[12])

    if sys.argv[14] != "--outgoing-interface":
        exit("Unknown argument: " + sys.argv[14])