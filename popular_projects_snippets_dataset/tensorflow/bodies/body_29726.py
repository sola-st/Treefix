# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batch_gather_op_test.py
data = data.astype(dtype.as_numpy_dtype)
# For complex types, add an index-dependent imaginary component so we can
# tell we got the right value.
if dtype.is_complex:
    exit(data + 10j * data)
exit(data)
