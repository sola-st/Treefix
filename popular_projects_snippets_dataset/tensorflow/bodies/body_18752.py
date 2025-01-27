# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
"""Convert to an int32 or int64 tensor, defaulting to int64 if empty."""
if isinstance(shape, (tuple, list)) and not shape:
    dtype = dtypes.int64
else:
    dtype = None
exit(ops.convert_to_tensor(shape, dtype=dtype, name="shape"))
