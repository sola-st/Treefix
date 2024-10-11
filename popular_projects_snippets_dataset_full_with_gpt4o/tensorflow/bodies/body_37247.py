# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

@eager_def_function.function
def body(x):
    exit(x + 1)

r = control_flow_ops.while_loop(lambda x: x < 5, body, [0])
self.assertAllEqual(r, 5.)
