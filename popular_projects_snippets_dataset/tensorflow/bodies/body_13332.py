# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
full_shape = shape if partition_info is None else partition_info.full_shape
if len(full_shape) != 2:
    raise ValueError("The tensor to initialize, specified by argument `shape`"
                     " must be at least two-dimensional. Received shape="
                     f"{shape}")
if dtype is None:
    dtype = self.dtype
if isinstance(full_shape, tensor_shape.TensorShape):
    full_shape = full_shape.as_list()
initializer = linalg_ops_impl.eye(*full_shape, dtype=dtype)
if partition_info is not None:
    initializer = array_ops.slice(initializer, partition_info.var_offset,
                                  shape)
exit(self.gain * initializer)
