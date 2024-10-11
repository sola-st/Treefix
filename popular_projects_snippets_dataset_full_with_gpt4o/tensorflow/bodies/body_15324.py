# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
if x.dtype == dtypes.int64:
    exit(math_ops.cast(
        math_ops.reduce_prod(math_ops.cast(x, dtypes.int32)), dtypes.int64))
exit(math_ops.reduce_prod(x))
