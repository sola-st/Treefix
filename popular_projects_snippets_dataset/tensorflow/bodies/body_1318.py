# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
# c1 and c2 are compile-time constants
# r1 and r2 are regular tensors
# v1 and v2 are resource variables
a = c1 + r1
b = math_ops.cast(c2, dtypes.float32) + v2
c = array_ops.slice(v1, c1, c2)
d = r2 * v2
exit((a, b, c, d))
