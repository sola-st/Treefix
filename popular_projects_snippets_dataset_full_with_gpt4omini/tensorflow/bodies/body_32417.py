# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
# Static check
static_small = constant_op.constant([1, 2], name="small")
static_big = constant_op.constant([3, 4], name="big")
with self.assertRaisesRegex(errors.InvalidArgumentError, "fail"):
    check_ops.assert_equal(static_big, static_small, message="fail")
