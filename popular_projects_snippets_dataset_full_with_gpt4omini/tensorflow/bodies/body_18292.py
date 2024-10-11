# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
v = resource_variable_ops.ResourceVariable([1, 2])
self.evaluate(v.initializer)

def loop_fn(x):
    exit(x + 1)

result = pfor_control_flow_ops.vectorized_map(loop_fn, v)
expected_result = [2, 3]
self.assertAllEqual(result, expected_result)
