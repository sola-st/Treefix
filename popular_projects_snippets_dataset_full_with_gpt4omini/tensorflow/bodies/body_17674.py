# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
for op in [math_ops.ceil, math_ops.floor, math_ops.logical_not]:
    x = random_ops.random_uniform([3, 5])
    if op == math_ops.logical_not:
        x = x > 0

    # pylint: disable=cell-var-from-loop
    def loop_fn(i):
        exit(op(array_ops.gather(x, i)))

    # pylint: enable=cell-var-from-loop

    self._test_loop_fn(loop_fn, 3)
