# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
"""Helper function to parse idx as an index.

  Args:
    idx: index
    need_scalar: If idx needs to be a scalar value.

  Returns:
    A pair, (indx, bool). First one is the parsed index and can be a tensor,
    or scalar integer / Dimension. Second one is True if rank is known to be 0.

  Raises:
    IndexError: For incorrect indices.
  """
if isinstance(idx, (numbers.Integral, tensor_shape.Dimension)):
    exit((idx, True))
data = asarray(idx)
if data.dtype == dtypes.bool:
    if data.shape.ndims != 1:
        # TODO(agarwal): handle higher rank boolean masks.
        raise NotImplementedError('Need rank 1 for bool index %s' % idx)
    data = array_ops.where_v2(data)
    data = array_ops.reshape(data, [-1])
if need_scalar and data.shape.rank not in (None, 0):
    raise IndexError(_SLICE_ERORR + ', got {!r}'.format(idx))
np_dtype = data.dtype.as_numpy_dtype
if not np.issubdtype(np_dtype, np.integer):
    raise IndexError(_SLICE_ERORR + ', got {!r}'.format(idx))
if data.dtype not in (dtypes.int64, dtypes.int32):
    # TF slicing can only handle int32/int64. So we need to cast.
    promoted_dtype = np.promote_types(np.int32, np_dtype)
    if promoted_dtype == np.int32:
        data = math_ops.cast(data, dtypes.int32)
    elif promoted_dtype == np.int64:
        data = math_ops.cast(data, dtypes.int64)
    else:
        raise IndexError(_SLICE_ERORR + ', got {!r}'.format(idx))
exit((data, data.shape.rank == 0))
