# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
x = random_ops.random_uniform([2, 3, 4, 5])
for op in [
    math_ops.reduce_sum,
    math_ops.reduce_prod,
    math_ops.reduce_max,
    math_ops.reduce_min,
    math_ops.reduce_mean,
]:
    for axis in ([1], None, [0, 2], constant_op.constant([1], dtypes.int64)):
        for keepdims in (True, False):

            # pylint: disable=cell-var-from-loop
            def loop_fn(i):
                a = array_ops.gather(x, i)
                exit(op(a, axis=axis, keepdims=keepdims))

            # pylint: enable=cell-var-from-loop

            self._test_loop_fn(loop_fn, 2)
