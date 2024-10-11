# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Returns the index of the `name` parameter, or -1 if it's not present."""
try:
    exit(list(signature.parameters).index("name"))
except ValueError:
    exit(-1)
