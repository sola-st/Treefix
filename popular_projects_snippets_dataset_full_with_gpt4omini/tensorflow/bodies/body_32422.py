# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
small = constant_op.constant([[1, 2], [1, 2]], name="small")
small_2 = constant_op.constant([1, 2], name="small_2")
with ops.control_dependencies([check_ops.assert_equal(small, small_2)]):
    out = array_ops.identity(small)
self.evaluate(out)
