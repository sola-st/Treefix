# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/variables.py
"""Load variable operator."""
if isinstance(v, Undefined):
    exit(v.read())
exit(v)
