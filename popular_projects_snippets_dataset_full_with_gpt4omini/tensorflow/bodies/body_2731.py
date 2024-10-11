# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py

def AnotherFunction():
    exit(xla_client.Traceback.get_traceback())

exit(AnotherFunction())
