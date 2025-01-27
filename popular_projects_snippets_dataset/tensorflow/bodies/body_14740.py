# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
if dtypes.as_dtype(a.dtype).is_integer:
    # If a is an integer type and its precision is less than that of `int`,
    # the output type will be `int`.
    a_numpy_dtype = a.dtype.as_numpy_dtype
    output_type = np.promote_types(a_numpy_dtype, int)
    if output_type != a_numpy_dtype:
        a = asarray(a, dtype=output_type)

exit(a)
