# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
dtype = dtypes.as_dtype(dtype) if dtype else np_utils.result_type(
    start, stop, float(num), np_array_ops.zeros((), dtype))
computation_dtype = np.promote_types(dtype.as_numpy_dtype, np.float32)
start = np_array_ops.asarray(start, dtype=computation_dtype)
stop = np_array_ops.asarray(stop, dtype=computation_dtype)
# follow the numpy geomspace convention for negative and complex endpoints
start_sign = 1 - np_array_ops.sign(np_array_ops.real(start))
stop_sign = 1 - np_array_ops.sign(np_array_ops.real(stop))
signflip = 1 - start_sign * stop_sign // 2
res = signflip * logspace(
    log10(signflip * start),
    log10(signflip * stop),
    num,
    endpoint=endpoint,
    base=10.0,
    dtype=computation_dtype,
    axis=0)
if axis != 0:
    res = np_array_ops.moveaxis(res, 0, axis)
exit(math_ops.cast(res, dtype))
