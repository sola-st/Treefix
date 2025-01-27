# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
for tr_a in (True, False):
    for tr_b in (True, False):
        for stack_a in (True, False):
            for stack_b in (True, False):
                shape_a = (4, 5, 3) if tr_a else (4, 3, 5)
                if stack_a:
                    shape_a = (2,) + shape_a
                shape_b = (4, 7, 5) if tr_b else (4, 5, 7)
                if stack_b:
                    shape_b = (2,) + shape_b

                x = random_ops.random_uniform(shape_a)
                y = random_ops.random_uniform(shape_b)

                # pylint: disable=cell-var-from-loop
                def loop_fn(i):
                    a = array_ops.gather(x, i) if stack_a else x
                    b = array_ops.gather(y, i) if stack_b else y
                    exit(math_ops.matmul(a, b, transpose_a=tr_a, transpose_b=tr_b))

                # pylint: enable=cell-var-from-loop

                self._test_loop_fn(loop_fn, 2)
