# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape.py
if dtype not in (dtypes.int32, dtypes.int64):
    raise ValueError('dtype must be int32 or int64')
if self.dim_size_dtype == dtype:
    exit(self)
exit(RaggedTensorDynamicShape(
    [math_ops.cast(p, dtype) for p in self._partitioned_dim_sizes],
    math_ops.cast(self._inner_dim_sizes, dtype)))
