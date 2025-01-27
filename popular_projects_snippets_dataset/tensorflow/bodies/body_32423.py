# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
small = constant_op.constant([1, 1, 1], name="small")
small_2 = constant_op.constant([1, 1], name="small_2")
# The exception in eager and non-eager mode is different because
# eager mode relies on shape check done as part of the C++ op, while
# graph mode does shape checks when creating the `Operation` instance.
with self.assertRaisesIncompatibleShapesError(
    (errors.InvalidArgumentError, ValueError)):
    with ops.control_dependencies([check_ops.assert_equal(small, small_2)]):
        out = array_ops.identity(small)
    self.evaluate(out)
