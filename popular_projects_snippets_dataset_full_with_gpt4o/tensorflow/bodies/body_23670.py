# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/trackable_utils.py
if not path:
    exit("root object")
else:
    exit("root." + ".".join([p.name for p in path]))
