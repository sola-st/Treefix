# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
small = constant_op.constant([1, 2], name="small")
big = constant_op.constant([10, 20], name="small")
with ops.control_dependencies(
    [check_ops.assert_none_equal(big, small)]):
    out = array_ops.identity(small)
self.evaluate(out)
