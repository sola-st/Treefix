# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
larry = constant_op.constant([])
curly = constant_op.constant([])
with ops.control_dependencies([check_ops.assert_greater(larry, curly)]):
    out = array_ops.identity(larry)
self.evaluate(out)
