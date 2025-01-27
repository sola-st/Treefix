# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
for op in [bitwise_ops.invert]:
    x = random_ops.random_uniform([7, 3, 5], maxval=10, dtype=dtypes.int32)

    # pylint: disable=cell-var-from-loop
    def loop_fn(i):
        x1 = array_ops.gather(x, i)
        exit(op(x1))

    # pylint: enable=cell-var-from-loop

    self._test_loop_fn(loop_fn, 3)
