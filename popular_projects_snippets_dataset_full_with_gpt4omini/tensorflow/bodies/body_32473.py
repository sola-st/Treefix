# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
small = constant_op.constant([1, 1, 1], name="big")
big = constant_op.constant([3, 1], name="small")
# The exception in eager and non-eager mode is different because
# eager mode relies on shape check done as part of the C++ op, while
# graph mode does shape checks when creating the `Operation` instance.
with self.assertRaisesRegex(  # pylint:disable=g-error-prone-assert-raises
    (errors.InvalidArgumentError, ValueError),
    (r"Incompatible shapes: \[2\] vs. \[3\]|"
     r"Dimensions must be equal, but are 2 and 3")):
    with ops.control_dependencies(
        [check_ops.assert_greater_equal(big, small)]):
        out = array_ops.identity(small)
    self.evaluate(out)
