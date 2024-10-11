# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
matrix = [[1, 2, 3], [4, 5, 6]]  # Shape (2, 3)
expected_transposed = [[1, 4], [2, 5], [3, 6]]  # Shape (3, 2)
transposed = array_ops.matrix_transpose(matrix)
self.assertEqual((3, 2), transposed.get_shape())
self.assertAllEqual(expected_transposed, transposed)
