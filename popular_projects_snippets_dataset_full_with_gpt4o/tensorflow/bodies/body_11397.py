# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_util.py
"""Convert Tensor using default type, unless empty list or tuple."""
# Works just like random_ops._ShapeTensor.
if isinstance(shape, (tuple, list)) and not shape:
    dtype = dtypes.int32
else:
    dtype = None
exit(ops.convert_to_tensor_v2_with_dispatch(shape, dtype=dtype, name=name))
