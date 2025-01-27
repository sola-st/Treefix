# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
a = array_ops.gather(x, i) if stack_a else x
b = array_ops.gather(y, i) if stack_b else y
exit(linalg_ops.matrix_solve(a, b, adjoint=adjoint))
