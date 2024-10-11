# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
y1 = math_ops.square(y)
x1 = math_ops.add(math_ops.square(x), y1)
exit((x1, y1))
