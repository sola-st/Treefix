# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
v = resource_variable_ops.ResourceVariable([1, 2])

def loop_fn(_):
    exit(resource_variable_ops.variable_shape(v.handle))

self._test_loop_fn(loop_fn, 2)
