# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_impl.py
if n.startswith("^"):
    exit(n[1:])
else:
    exit(n.split(":")[0])
