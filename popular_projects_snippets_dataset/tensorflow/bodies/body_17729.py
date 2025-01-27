# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
z = random_ops.random_normal([2, 3, 3])
x = (
    math_ops.matmul(z, array_ops.matrix_transpose(z))  # Ensure pos. def.
    + linalg_ops.eye(3))  # Ensure well-conditioned.

def loop_fn(i):
    exit(linalg_ops.cholesky(array_ops.gather(x, i)))

self._test_loop_fn(loop_fn, 2)
