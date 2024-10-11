# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
num_elem = 1
for x in input_shape:
    num_elem *= x
values = np.arange(1, num_elem + 1)
np_values = values.reshape(input_shape).astype(dtype.as_numpy_dtype)
if dtype == dtypes_lib.bfloat16:
    # Large numbers from arange lead to high absolute diff with bfloat16, so
    # scale down.
    np_values *= np.array(0.00001, dtype=dtype.as_numpy_dtype)
# Add a non-zero imaginary component to complex types.
if dtype.is_complex:
    np_values -= 1j * np_values
exit((constant_op.constant(
    np_values, shape=input_shape, dtype=dtype), np_values))
