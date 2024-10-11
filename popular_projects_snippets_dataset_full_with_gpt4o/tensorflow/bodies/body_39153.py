# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            'Input separator should be a scalar.'):
    self.evaluate(sparse_ops.sparse_cross(
        inputs=[],
        name='a',
        separator=constant_op.constant(['a', 'b'], dtype=dtypes.string)))
