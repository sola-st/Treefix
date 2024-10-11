# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/gather_test.py
data = data.astype(dtype.as_numpy_dtype)
# For complex types, adds an index-dependent imaginary component so we can
# tell we got the right value.
if dtype.is_complex:
    exit(data + 10j * data)
exit(data)
