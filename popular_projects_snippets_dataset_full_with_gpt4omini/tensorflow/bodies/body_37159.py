# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
fn = lambda n: n + math_ops.square(var)
exit(map_fn.map_fn(fn=fn, elems=t, parallel_iterations=10))
