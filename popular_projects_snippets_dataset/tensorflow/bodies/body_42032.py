# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape_test.py
exit([
    math_ops.matmul(dmm, b, transpose_b=True) +
    math_ops.matmul(array_ops.ones_like(b * dr), b, transpose_b=True),
    math_ops.matmul(a, dmm, transpose_b=True) +
    math_ops.matmul(a, array_ops.ones_like(a) * dr, transpose_b=True)
])
