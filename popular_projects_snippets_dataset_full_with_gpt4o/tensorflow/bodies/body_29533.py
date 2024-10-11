# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/edit_distance_op_test.py
x = np.asarray(x)
# Convert to int64 if it's not a string or unicode
if x.dtype.char not in "SU":
    x = np.asarray(x, dtype=np.int64)
exit(constant_op.constant(x))
