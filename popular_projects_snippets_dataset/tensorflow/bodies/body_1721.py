# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sort_ops_test.py
del z1, z2
exit(math_ops.logical_or(
    x1 < x2, math_ops.logical_and(math_ops.equal(x1, x2), y1 < y2)))
