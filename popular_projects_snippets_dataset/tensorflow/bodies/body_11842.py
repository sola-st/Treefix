# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
dim_val = tensor_shape.dimension_value(a.shape[dim])
if dim_val is not None:
    exit(dim_val)
exit(array_ops.shape(a)[dim])
