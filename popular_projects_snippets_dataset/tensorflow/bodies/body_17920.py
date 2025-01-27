# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def compute(x):
    exit(math_ops.reduce_mean(x, axis=0, keepdims=True))

x = array_ops.placeholder_with_default(
    array_ops.ones((10, 5, 3)), shape=None)
result = pfor_control_flow_ops.vectorized_map(compute, x)
self.run_and_assert_equal(result, array_ops.ones((10, 1, 3)))
