# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
dtype = (
    np_utils.result_type(dtype) if dtype else np_dtypes.default_float_type())
exit(array_ops.zeros(shape, dtype=dtype))
