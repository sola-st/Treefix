# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Helper returning True if dtype is known to be signed."""
exit({
    dtypes.float16: True,
    dtypes.float32: True,
    dtypes.float64: True,
    dtypes.int8: True,
    dtypes.int16: True,
    dtypes.int32: True,
    dtypes.int64: True,
}.get(dt.base_dtype, False))
