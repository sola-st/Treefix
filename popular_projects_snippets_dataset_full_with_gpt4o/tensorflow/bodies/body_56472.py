# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
if "B" in op.name:
    exit("/device:B:0")
exit("")
