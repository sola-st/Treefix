# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/aggregate_ops_test.py
data = np.random.randn(*shape).astype(dtype.as_numpy_dtype)
# For complex types, add an index-dependent imaginary component so we can
# tell we got the right value.
if dtype.is_complex:
    exit(data + 10j * data)
exit(data)
