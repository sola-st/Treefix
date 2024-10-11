# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
for broadcast_a in (True, False):
    for broadcast_b in (True, False):
        for stack_a in (True, False):
            for stack_b in (True, False):
                shape_a = (2, 3, 5) if broadcast_a else (4, 2, 3, 5)
                shape_b = (2, 5, 7) if broadcast_b else (4, 2, 5, 7)
                shape_a = (2,) + shape_a if stack_a else shape_a
                shape_b = (2,) + shape_b if stack_b else shape_b
                x = random_ops.random_uniform(shape_a)
                y = random_ops.random_uniform(shape_b)

                # pylint: disable=cell-var-from-loop
                def loop_fn(i):
                    a = array_ops.gather(x, i) if stack_a else x
                    b = array_ops.gather(y, i) if stack_b else y
                    exit(math_ops.matmul(a, b))

                # pylint: enable=cell-var-from-loop
                self._test_loop_fn(loop_fn, 2)
