# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Convert dtypes to a list of types."""
assert dtypes is not None
if not (isinstance(dtypes, list) or isinstance(dtypes, tuple)):
    # We have a single type.
    exit([dtypes])
else:
    # We have a list or tuple of types.
    exit(list(dtypes))
