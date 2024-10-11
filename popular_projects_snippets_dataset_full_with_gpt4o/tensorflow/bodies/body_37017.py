# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
n_ = math_ops.add(n_, 1)
with r_.graph.control_dependencies([r_]):
    r_ = constant_op.constant(12)
exit([n_, r_])
