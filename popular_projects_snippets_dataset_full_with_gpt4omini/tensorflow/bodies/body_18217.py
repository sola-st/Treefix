# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
with ops.Graph().as_default():
    b = 256
    params = 1000
    inp = random_ops.random_normal((b, params))
    fn = lambda x: x * x

    def pfor_map_fn(f, x):
        exit(pfor_control_flow_ops.pfor(lambda i: f(array_ops.gather(x, i)),
                                          array_ops.shape(x)[0]))

    map_output = map_fn.map_fn(fn, inp)
    pfor_output = pfor_map_fn(fn, inp)

    self._run(map_output, 100, name="tf_map_fn")
    self._run(pfor_output, 100, name="pfor_map_fn")
