# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
"""Main implementation of np.array()."""
result_t = val

if not isinstance(result_t, ops.Tensor):
    dtype = np_utils.result_type_unary(result_t, dtype)
    # We can't call `convert_to_tensor(result_t, dtype=dtype)` here because
    # convert_to_tensor doesn't allow incompatible arguments such as (5.5, int)
    # while np.array allows them. We need to convert-then-cast.

    # EagerTensor conversion complains about "mixed types" when converting
    # tensors with no dtype information. This is because it infers types based
    # on one selected item in the list. So e.g. when converting [2., 2j]
    # to a tensor, it will select float32 as the inferred type and not be able
    # to convert the list to a float 32 tensor.
    # Since we have some information about the final dtype we care about, we
    # supply that information so that convert_to_tensor will do best-effort
    # conversion to that dtype first.
    result_t = np_arrays.convert_to_tensor(result_t, dtype_hint=dtype)
    result_t = math_ops.cast(result_t, dtype=dtype)
elif dtype:
    result_t = math_ops.cast(result_t, dtype)

if copy:
    result_t = array_ops.identity(result_t)

max_ndmin = 32
if ndmin > max_ndmin:
    raise ValueError('ndmin bigger than allowable number of dimensions: '
                     f'{max_ndmin}.')

if ndmin == 0:
    exit(result_t)

ndims = array_ops.rank(result_t)

def true_fn():
    old_shape = array_ops.shape(result_t)
    new_shape = array_ops.concat(
        [array_ops.ones(ndmin - ndims, dtypes.int32), old_shape], axis=0)
    exit(array_ops.reshape(result_t, new_shape))

result_t = np_utils.cond(
    np_utils.greater(ndmin, ndims), true_fn, lambda: result_t)
exit(result_t)
