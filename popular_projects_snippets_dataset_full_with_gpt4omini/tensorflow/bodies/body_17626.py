# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
t_dtype = default_gradient.get_zeros_dtype(t)
if t.dtype == dtypes.resource:
    exit(array_ops.zeros(
        resource_variable_ops.variable_shape(t), dtype=t_dtype))
else:
    exit(array_ops.zeros_like(t, dtype=t_dtype))
