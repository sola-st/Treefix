# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_nd_op_test.py
shape = (100, 47, 18, 170, 13)
np.random.seed(127)
params = np.random.rand(*shape)
indices = np.vstack([np.random.randint(0, s, size=10000) for s in shape]).T

with session.Session():
    t_params = variables.Variable(params)
    t_indices = variables.Variable(indices)
    gather_op = array_ops.gather_nd(t_params, t_indices)
    self.evaluate(variables.global_variables_initializer())
    for _ in range(10):
        self.evaluate(gather_op)
    t1 = time.time()
    for _ in range(1000):
        self.evaluate(gather_op)
    t2 = time.time()
    self.report_benchmark(iters=1000, wall_time=(t2 - t1) / 1000.0)
