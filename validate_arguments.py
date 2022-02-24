import sys

def validate_check():
    if sys.argv[1] != "--interface-name":
        exit("Unknown argument: " + sys.argv[1])

    if sys.argv[3] != "--config-path":
        exit("Unknown argument: " + sys.argv[3])