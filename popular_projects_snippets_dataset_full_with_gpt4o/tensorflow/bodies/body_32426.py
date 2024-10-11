# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
larry = constant_op.constant([])
check_op = check_ops.assert_equal(larry, larry)
if context.executing_eagerly():
    self.assertIs(check_op, None)
else:
    self.assertEqual(check_op.type, "NoOp")
