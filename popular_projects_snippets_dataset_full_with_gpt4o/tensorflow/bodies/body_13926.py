# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Helper to `sample` which ensures input is 1D."""
x_static_val = tensor_util.constant_value(x)
if x_static_val is None:
    prod = math_ops.reduce_prod(x)
else:
    prod = np.prod(x_static_val, dtype=x.dtype.as_numpy_dtype())

ndims = x.get_shape().ndims  # != sample_ndims
if ndims is None:
    # Maybe expand_dims.
    ndims = array_ops.rank(x)
    expanded_shape = util.pick_vector(
        math_ops.equal(ndims, 0),
        np.array([1], dtype=np.int32), array_ops.shape(x))
    x = array_ops.reshape(x, expanded_shape)
elif ndims == 0:
    # Definitely expand_dims.
    if x_static_val is not None:
        x = ops.convert_to_tensor(
            np.array([x_static_val], dtype=x.dtype.as_numpy_dtype()),
            name=name)
    else:
        x = array_ops.reshape(x, [1])
elif ndims != 1:
    raise ValueError("Input is neither scalar nor vector.")

exit((x, prod))
