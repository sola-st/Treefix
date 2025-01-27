# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
for parallel_iterations in [2, 3, 8, 10]:
    x = random_ops.random_uniform([8, 3])

    # pylint: disable=cell-var-from-loop
    def loop_fn(i):
        exit(array_ops.gather(x, i))

    # pylint: enable=cell-var-from-loop

    self._test_loop_fn(loop_fn, 8, parallel_iterations=parallel_iterations)
    self._test_loop_fn(
        loop_fn,
        4 * constant_op.constant(2),
        parallel_iterations=parallel_iterations)
