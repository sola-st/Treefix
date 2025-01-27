# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
x_const = constant_op.constant(ops.get_collection("x")[0])
y_const = constant_op.constant(ops.get_collection("y")[0])
exit(math_ops.add(x_const, y_const))
