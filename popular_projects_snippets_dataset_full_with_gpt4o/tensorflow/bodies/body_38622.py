# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bucketize_op_test.py
op = math_ops._bucketize(
    constant_op.constant([-5, 0]), boundaries=[0, 8, 3, 11])
with self.session():
    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "Expected sorted boundaries"):
        self.evaluate(op)
