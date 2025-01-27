# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
x = rng.rand(3)
y = rng.rand(1, 1)

with self.assertRaisesRegex(ValueError, "at least two dimensions"):
    linear_operator_util.broadcast_matrix_batch_dims([x, y])

with self.assertRaisesRegex(ValueError, "at least two dimensions"):
    linear_operator_util.broadcast_matrix_batch_dims([y, x])
