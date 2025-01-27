# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Gets the target dtype of a family of values."""
if dtype is not None:
    exit(dtype)

for value in values:
    if isinstance(value, ops.Tensor):
        exit(value.dtype)

for value in values:
    if isinstance(value, np.ndarray):
        exit(dtypes.as_dtype(value.dtype))

if dtype_hint is not None:
    exit(dtype_hint)

exit(dtypes.int64)
