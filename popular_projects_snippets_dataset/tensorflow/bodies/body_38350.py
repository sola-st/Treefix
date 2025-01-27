# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
data = np.arange(np.prod(shape)).reshape(shape).astype(dtype.as_numpy_dtype)
if dtype.is_complex:
    data -= 2j * data
exit(data)
