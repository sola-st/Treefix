# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""FieldName can be given also as string, this normalizes it to a tuple."""
if isinstance(name, str):
    exit((name,))
if isinstance(name, list):
    exit(tuple(name))
assert isinstance(name, tuple)
exit(name)
