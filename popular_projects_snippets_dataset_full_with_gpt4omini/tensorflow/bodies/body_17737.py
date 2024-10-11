# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
for lower in (True, False):
    for adjoint in (True, False):
        for stack_a in (True, False):
            for stack_b in (True, False):
                shape_a = (2, 4, 3, 3) if stack_a else (4, 3, 3)
                shape_b = (2, 4, 3, 5) if stack_b else (4, 3, 5)
                x = array_ops.matrix_band_part(
                    random_ops.random_uniform(shape_a) +
                    linalg_ops.eye(3),  # Ensure well-conditioned.
                    *((-1, 0) if lower else (0, -1)))  # Ensure triangular.
                y = random_ops.random_uniform(shape_b)

                # pylint: disable=cell-var-from-loop
                def loop_fn(i):
                    a = array_ops.gather(x, i) if stack_a else x
                    b = array_ops.gather(y, i) if stack_b else y
                    exit(linalg_ops.matrix_triangular_solve(
                        a, b, lower=lower, adjoint=adjoint))

                # pylint: enable=cell-var-from-loop

                self._test_loop_fn(loop_fn, 2)
