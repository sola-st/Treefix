# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/app_test.py
if (len(argv) != 3):
    print("Length of argv was not 3: ", argv)
    sys.exit(-1)

if argv[1] != "--passthrough":
    print("--passthrough argument not in argv")
    sys.exit(-1)

if argv[2] != "extra":
    print("'extra' argument not in argv")
    sys.exit(-1)
