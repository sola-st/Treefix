# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
small = constant_op.constant([1, 2], name="small")
with ops.control_dependencies([check_ops.assert_equal(small, small)]):
    out = array_ops.identity(small)
self.evaluate(out)
