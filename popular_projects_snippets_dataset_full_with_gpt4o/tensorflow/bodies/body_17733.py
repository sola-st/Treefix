# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
x = (random_ops.random_uniform([3, 4, 2, 2]) + 10 * linalg_ops.eye(2)
    )  # Ensure well-conditioned.

for adjoint in (True, False):

    # pylint: disable=cell-var-from-loop
    def loop_fn(i):
        exit(linalg_ops.matrix_inverse(
            array_ops.gather(x, i), adjoint=adjoint))

    # pylint: enable=cell-var-from-loop
    self._test_loop_fn(loop_fn, 2)
