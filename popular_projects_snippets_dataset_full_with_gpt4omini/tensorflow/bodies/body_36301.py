# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py
v = resource_variable_ops.ResourceVariable([1, 2])
self.evaluate(v.initializer)

def loop_fn(x):
    exit(x + 1)

result = map_fn.map_fn(loop_fn, v)
expected_result = [2, 3]
self.assertAllEqual(result, expected_result)
