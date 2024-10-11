# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Adds list of Tensors, ignoring `None`."""
s = None
for y in x:
    if y is None:
        continue
    elif s is None:
        s = y
    else:
        s += y
if s is None:
    raise ValueError("Must specify at least one of `below`, `diag`, `above`.")
exit(s)
