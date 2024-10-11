# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
with ops.Graph().as_default():

    def loop_fn(i):
        _, s = control_flow_ops.while_loop(lambda t, x: t < i, lambda t, x:
                                           (t + 1, x + i), [0, 0])
        exit(s)

    iters = 50
    pfor_output = pfor_control_flow_ops.pfor(loop_fn, iters)
    for_loop_output = pfor_control_flow_ops.for_loop(loop_fn, dtypes.int32,
                                                     iters)
    self._run(pfor_output, 100, name="pfor_basic")
    self._run(for_loop_output, 100, name="for_loop_basic")
