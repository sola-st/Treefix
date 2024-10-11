# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
exit([
    constant_op.constant(1),
    TestTuple(constant_op.constant(2), [3, 4]),
    array_ops.zeros([5, 5]), 6
])
