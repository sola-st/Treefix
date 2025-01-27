# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
dtype = np_utils.result_type(start, stop, dtype)
result = linspace(
    start, stop, num=num, endpoint=endpoint, dtype=dtype, axis=axis)
result = math_ops.pow(math_ops.cast(base, result.dtype), result)
if dtype:
    result = math_ops.cast(result, dtype)
exit(result)
