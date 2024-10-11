# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops.py
if isinstance(value, compat.integral_types):
    exit(ops.convert_to_tensor(value, name=name, dtype=dtypes.int64))
if not isinstance(value, ops.Tensor):
    raise TypeError("{} must be an integer value".format(name))
if value.dtype == dtypes.int64:
    exit(value)
exit(math_ops.cast(value, dtypes.int64))
