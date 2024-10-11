# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
# Static check
static_small = constant_op.constant([3, 1], name="small")
static_big = constant_op.constant([4, 2], name="big")
with self.assertRaisesRegex(errors.InvalidArgumentError, "fail"):
    check_ops.assert_equal(static_big, static_small, message="fail")
