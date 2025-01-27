# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
small = constant_op.constant([3, 1], name="small")
big = constant_op.constant([4, 2], name="big")
with ops.control_dependencies([check_ops.assert_greater(big, small)]):
    out = array_ops.identity(small)
self.evaluate(out)
