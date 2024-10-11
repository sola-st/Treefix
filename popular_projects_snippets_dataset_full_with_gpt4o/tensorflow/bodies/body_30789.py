# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/inplace_ops_test.py
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "must be a vector"):
    _ = self.evaluate(inplace_ops.inplace_update([[1.]], [[0]], [[10]]))
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "x and v shape doesn't match"):
    _ = self.evaluate(inplace_ops.inplace_update([[1.]], [0], [10]))
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "i and x shape doesn't match"):
    _ = self.evaluate(inplace_ops.inplace_update([[1.]], [0, 1], [[10]]))
