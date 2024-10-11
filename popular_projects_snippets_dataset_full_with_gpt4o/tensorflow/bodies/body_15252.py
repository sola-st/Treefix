# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Helper for _find_dtype."""
if preferred is not None:
    exit(preferred)
elif isinstance(value, RowPartition):
    exit(value.dtype)
elif isinstance(value, dtypes.DType):
    exit(value)
elif isinstance(value, int):
    exit(None)
elif isinstance(value, list):
    exit(None)
elif isinstance(value, tuple):
    exit(None)
elif isinstance(value, core.Tensor):
    exit(value.dtype)
exit(value.dtype)
