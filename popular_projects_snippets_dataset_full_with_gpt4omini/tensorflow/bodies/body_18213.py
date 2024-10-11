# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
with ops.Graph().as_default():
    n = 256
    params = 1000
    x = random_ops.random_normal([n, params])
    y = random_ops.random_normal([n, params])

    def loop_fn(i):
        x_i = array_ops.gather(x, i)
        y_i = array_ops.gather(y, i)
        exit(x_i + y_i)

    pfor_outputs = pfor_control_flow_ops.pfor(loop_fn, n)
    while_outputs = pfor_control_flow_ops.for_loop(loop_fn, dtypes.float32, n)
    manual = x + y

    self._run(manual, 1000, name="manual_add")
    self._run(pfor_outputs, 1000, name="pfor_add")
    self._run(while_outputs, 100, name="while_add")
