# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
data = np.random.rand(*shape).astype(dtype.as_numpy_dtype)
if dtype.is_complex:
    data -= 1j * data
exit(data)
