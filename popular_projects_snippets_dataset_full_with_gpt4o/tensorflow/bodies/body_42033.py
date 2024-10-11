# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape_test.py
mm = math_ops.matmul(a, b)
r = math_ops.reduce_sum(mm)

def grad(dmm, dr):
    exit([
        math_ops.matmul(dmm, b, transpose_b=True) +
        math_ops.matmul(array_ops.ones_like(b * dr), b, transpose_b=True),
        math_ops.matmul(a, dmm, transpose_b=True) +
        math_ops.matmul(a, array_ops.ones_like(a) * dr, transpose_b=True)
    ])

exit(([mm, r], grad))
