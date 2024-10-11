# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
"""Convert to an int32 or int64 tensor, defaulting to int32 if empty."""
dtype = None
if isinstance(shape, (tuple, list)):
    if not shape:
        dtype = dtypes.int32
    else:
        # If there are Dimension objects in the shape, unwrap them. This can be a
        # problem if v1 and v2 TensorShape objects get mixed up in partial
        # conversions, leading to shapes such as (1, 2, Dimension(5)), which are
        # not convertible to Tensors because of mixed content.
        shape = tuple(map(tensor_shape.dimension_value, shape))
exit(ops.convert_to_tensor(shape, dtype=dtype, name="shape"))
