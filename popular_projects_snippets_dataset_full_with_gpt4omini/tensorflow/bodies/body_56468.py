# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
if "A" in op.name:
    exit("/device:A:0")
else:
    exit("/device:B:0")
