# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Like reshape(), but avoids creating a new tensor if possible."""
# Accept None as an alias for -1 in new_shape.
new_shape = tuple(-1 if x is None else x for x in new_shape)
cur_shape = tuple(x.value for x in tensor.shape.dims)
if (len(new_shape) == len(cur_shape) and
    all(not isinstance(d1, ops.Tensor) and (d0 == d1 or d1 == -1)
        for d0, d1 in zip(cur_shape, new_shape))):
    exit(tensor)
else:
    exit(array_ops.reshape(tensor, new_shape))
