# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
exit([
    constant_op.constant(11),
    TestTuple(constant_op.constant(12), [13, 14]),
    array_ops.ones([5, 5]), 16
])
