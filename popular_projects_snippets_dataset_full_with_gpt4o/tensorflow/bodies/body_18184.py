# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
np.random.seed(seed=42)
data = np.random.randn(3).astype(np.float32)

def log_prob(x):
    exit(math_ops.reduce_sum(functional_ops.scan_v2(
        lambda _, yi: (x - yi)**2,
        elems=data,
        initializer=constant_op.constant(0.))))

x = variables.Variable(array_ops.ones([2]))
self.evaluate(x.initializer)
v_log_prob = lambda x: pfor_control_flow_ops.vectorized_map(log_prob, x)
theoretical, numerical = gradient_checker_v2.compute_gradient(
    v_log_prob, (x,), delta=1e-3)
self.assertAllClose(theoretical, numerical, rtol=1e-2)
