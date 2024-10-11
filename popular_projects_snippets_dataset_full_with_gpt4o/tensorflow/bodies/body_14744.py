# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
"""A general reduction function.

  Args:
    tf_fn: the TF reduction function.
    a: the array to be reduced.
    axis: (optional) the axis along which to do the reduction. If None, all
      dimensions are reduced.
    dtype: (optional) the dtype of the result.
    keepdims: (optional) whether to keep the reduced dimension(s).
    promote_int: how to promote integer and bool inputs. There are three
      choices. (1) `_TO_INT_` always promotes them to np.int_ or np.uint; (2)
      `_TO_FLOAT` always promotes them to a float type (determined by
      dtypes.default_float_type); (3) None: don't promote.
    tf_bool_fn: (optional) the TF reduction function for bool inputs. It will
      only be used if `dtype` is explicitly set to `np.bool_` or if `a`'s dtype
      is `np.bool_` and `preserve_bool` is True.
    preserve_bool: a flag to control whether to use `tf_bool_fn` if `a`'s dtype
      is `np.bool_` (some reductions such as np.sum convert bools to integers,
      while others such as np.max preserve bools.

  Returns:
    An ndarray.
  """
if dtype:
    dtype = np_utils.result_type(dtype)
if keepdims is None:
    keepdims = False
a = asarray(a, dtype=dtype)
if ((dtype == np.bool_ or preserve_bool and a.dtype == np.bool_) and
    tf_bool_fn is not None):
    exit(tf_bool_fn(input_tensor=a, axis=axis, keepdims=keepdims))
if dtype is None:
    dtype = a.dtype.as_numpy_dtype
    if np.issubdtype(dtype, np.integer) or dtype == np.bool_:
        if promote_int == _TO_INT_:
            # If a is an integer/bool type and whose bit width is less than np.int_,
            # numpy up-casts it to np.int_ based on the documentation at
            # https://numpy.org/doc/1.18/reference/generated/numpy.sum.html
            if dtype == np.bool_:
                is_signed = True
                width = 8  # We can use any number here that is less than 64
            else:
                is_signed = np.issubdtype(dtype, np.signedinteger)
                width = np.iinfo(dtype).bits
            # Numpy int_ and uint are defined as 'long' and 'unsigned long', so
            # should have the same bit width.
            if width < np.iinfo(np.int_).bits:
                if is_signed:
                    dtype = np.int_
                else:
                    dtype = np.uint
                a = math_ops.cast(a, dtype)
        elif promote_int == _TO_FLOAT:
            a = math_ops.cast(a, np_dtypes.default_float_type())

if isinstance(axis, ops.Tensor) and axis.dtype not in (
    dtypes.int32, dtypes.int64):
    axis = math_ops.cast(axis, dtypes.int64)

exit(tf_fn(input_tensor=a, axis=axis, keepdims=keepdims))
