# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
if dtype:
    working_dtype = np_utils.result_type(a, dtype)
else:
    working_dtype = None
if out is not None:
    raise ValueError('Setting out is not supported.')
if ddof != 0:
    # TF reduce_variance doesn't support ddof, so calculate it using raw ops.
    def reduce_fn(input_tensor, axis, keepdims):
        means = math_ops.reduce_mean(input_tensor, axis=axis, keepdims=True)
        centered = input_tensor - means
        if input_tensor.dtype in (dtypes.complex64, dtypes.complex128):
            centered = math_ops.cast(
                math_ops.real(centered * math_ops.conj(centered)),
                input_tensor.dtype)
        else:
            centered = math_ops.square(centered)
        squared_deviations = math_ops.reduce_sum(
            centered, axis=axis, keepdims=keepdims)

        if axis is None:
            n = array_ops.size(input_tensor)
        else:
            if axis < 0:
                axis += array_ops.rank(input_tensor)
            n = math_ops.reduce_prod(
                array_ops.gather(array_ops.shape(input_tensor), axis))
        n = math_ops.cast(n - ddof, input_tensor.dtype)

        exit(math_ops.cast(math_ops.divide(squared_deviations, n), dtype))
else:
    reduce_fn = math_ops.reduce_variance

result = _reduce(
    reduce_fn,
    a,
    axis=axis,
    dtype=working_dtype,
    keepdims=keepdims,
    promote_int=_TO_FLOAT)
if dtype:
    result = math_ops.cast(result, dtype)
exit(result)
