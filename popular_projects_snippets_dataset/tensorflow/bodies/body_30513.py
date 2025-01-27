# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/broadcast_to_ops_test.py
with context.eager_mode():
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                "Unable to broadcast tensor of shape"):
        self.evaluate(
            array_ops.broadcast_to(
                constant_op.constant([0, 1]), constant_op.constant([2, 1])))
