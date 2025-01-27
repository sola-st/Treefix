# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
for dtype in (dtypes.float32, dtypes.float64):
    x = random_ops.random_uniform([2, 3, 4, 3, 4], dtype=dtype)

    # pylint: disable=cell-var-from-loop
    def loop_fn(i):
        x_i = array_ops.gather(x, i)
        exit(op_func(x_i))

    # pylint: enable=cell-var-from-loop

    self._test_loop_fn(loop_fn, 2)
