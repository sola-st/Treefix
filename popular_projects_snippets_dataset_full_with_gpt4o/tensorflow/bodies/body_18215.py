# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
with ops.Graph().as_default():
    n = 1024
    params = 1000
    x = random_ops.random_normal([n, params])
    y = random_ops.random_normal([params, params])

    def loop_fn(i):
        x_i = array_ops.expand_dims(array_ops.gather(x, i), 0)
        exit(math_ops.matmul(x_i, y))

    pfor_outputs = pfor_control_flow_ops.pfor(loop_fn, n)
    while_outputs = pfor_control_flow_ops.for_loop(loop_fn, dtypes.float32, n)
    manual = math_ops.matmul(x, y)

    self._run(manual, 1000, name="manual_matmul")
    self._run(pfor_outputs, 1000, name="pfor_matmul")
    self._run(while_outputs, 100, name="while_matmul")
