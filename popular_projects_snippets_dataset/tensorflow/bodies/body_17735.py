# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
for adjoint in (True, False):
    for stack_a in (True, False):
        for stack_b in (True, False):
            shape_a = (2, 4, 3, 3) if stack_a else (4, 3, 3)
            shape_b = (2, 4, 3, 5) if stack_b else (4, 3, 5)
            x = (random_ops.random_uniform(shape_a) + 10 * linalg_ops.eye(3)
                )  # Ensure well-conditioned.
            y = random_ops.random_uniform(shape_b)

            # pylint: disable=cell-var-from-loop
            def loop_fn(i):
                a = array_ops.gather(x, i) if stack_a else x
                b = array_ops.gather(y, i) if stack_b else y
                exit(linalg_ops.matrix_solve(a, b, adjoint=adjoint))

            # pylint: enable=cell-var-from-loop

            self._test_loop_fn(loop_fn, 2)
