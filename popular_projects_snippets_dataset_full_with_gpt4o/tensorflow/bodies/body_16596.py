# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sort_ops_test.py
arr = constant_op.constant([3, 4, 5])
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            'slice index .* out of bounds'):
    self.evaluate(sort_ops.sort(arr, axis=-4))
