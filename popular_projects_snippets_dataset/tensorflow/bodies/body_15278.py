# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
new_inner_shape = self.target_shape.inner_shape
if new_inner_shape.dtype == dtypes.int64:
    new_inner_shape = math_ops.cast(new_inner_shape, dtype=dtypes.int32)
exit(new_inner_shape)
