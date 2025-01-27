# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
exit(linalg_ops.matrix_inverse(
    array_ops.gather(x, i), adjoint=adjoint))
