# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
for x_shape in ([3, 4, 2, 2], [3, 2, 2]):
    x = random_ops.random_normal(x_shape)

    # pylint: disable=cell-var-from-loop
    def loop_fn(i):
        exit(linalg_ops.log_matrix_determinant(array_ops.gather(x, i)))

    # pylint: enable=cell-var-from-loop

    self._test_loop_fn(loop_fn, 3)
