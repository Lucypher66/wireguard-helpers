import sys

def validate_check():
    if sys.argv[1] != "--interface-name":
        exit("Unknown argument: " + sys.argv[1])

    if sys.argv[3] != "--config-path":
        exit("Unknown argument: " + sys.argv[3])

    if sys.argv[5] != "--interface-address":
        exit("Unknown argument: " + sys.argv[5])

    if sys.argv[7] != "--interface-subnetmask":
        exit("Unknown argument: " + sys.argv[7])

    if sys.argv[9] != "--save-config":
        exit("Unknown argument: " + sys.argv[9])

    if sys.argv[11] != "--local-listen-port":
        exit("Unknown argument: " + sys.argv[11])

    if sys.argv[13] != "--peer-pubkey":
        exit("Unknown argument: " + sys.argv[13])

    if sys.argv[15] != "--tunnel-ips":
        exit("Unknown argument: " + sys.argv[15])

    if sys.argv[17] != "--tunnel-subnetmask":
        exit("Unknown argument: " + sys.argv[17])

    if sys.argv[19] != "--peer-ip-or-domain":
        exit("Unknown argument: " + sys.argv[19])

    if sys.argv[21] != "--peer-listen-port":
        exit("Unknown argument: " + sys.argv[21])

    if sys.argv[23] != "--set-keepalive":
        exit("Unknown argument: " + sys.argv[23])

    if sys.argv [25] != "--keepalive-seconds":
        exit("Unknown argument: " + sys.argv[25])