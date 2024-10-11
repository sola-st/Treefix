# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
x = random_ops.random_uniform([2, 3, 4, 5])
for axis in (1, -2, constant_op.constant(1, dtypes.int64)):
    for exclusive in (True, False):
        for reverse in (True, False):

            # pylint: disable=cell-var-from-loop
            def loop_fn(i):
                a = array_ops.gather(x, i)
                exit(math_ops.cumprod(
                    a, axis=axis, exclusive=exclusive, reverse=reverse))

            # pylint: enable=cell-var-from-loop

            self._test_loop_fn(loop_fn, 2)
