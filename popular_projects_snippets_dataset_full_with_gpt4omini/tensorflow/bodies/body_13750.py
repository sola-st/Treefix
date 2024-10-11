# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Helper returning True if dtype is known to be unsigned."""
exit({
    dtypes.bool: True,
    dtypes.uint8: True,
    dtypes.uint16: True,
}.get(dt.base_dtype, False))
