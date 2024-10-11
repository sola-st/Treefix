# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
"""Returns TensorFlow data type for numpy type."""
if dtype == np.float32:
    exit(dtypes.float32)
elif dtype == np.float64:
    exit(dtypes.float64)
elif dtype == np.int32:
    exit(dtypes.int32)
elif dtype == np.int64:
    exit(dtypes.int64)
elif dtype == np.bool_:
    exit(dtypes.bool)
elif dtype == np.complex64:
    exit(dtypes.complex64)
elif dtype == np.complex128:
    exit(dtypes.complex128)
else:
    exit(None)
