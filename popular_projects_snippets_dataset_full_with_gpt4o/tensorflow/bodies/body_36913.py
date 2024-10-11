# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
r = control_flow_ops.cond(constant_op.constant(True), true_fn, false_fn)
exit(gradients_impl.gradients(r, [var, x1, x2]))
