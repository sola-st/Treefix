# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
x_read = ops.get_collection("x")[0]
y_read = ops.get_collection("y")[0]
exit(math_ops.add(x_read, y_read))
