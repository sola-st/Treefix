# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
z = random_ops.random_normal([2, 3, 3])
x = z + array_ops.matrix_transpose(z)  # Ensure self-adjoint.

def loop_fn(i):
    exit((linalg_ops.self_adjoint_eig(array_ops.gather(x, i)),
            linalg_ops.self_adjoint_eigvals(array_ops.gather(x, i))))

self._test_loop_fn(loop_fn, 2)
