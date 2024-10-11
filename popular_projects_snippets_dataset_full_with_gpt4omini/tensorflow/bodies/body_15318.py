# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""element to a string within a list."""
if x is Ellipsis:
    exit("...")
if isinstance(x, str):
    exit("'" + x + "'")
exit(str(x))
