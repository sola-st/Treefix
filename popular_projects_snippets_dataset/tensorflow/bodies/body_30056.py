# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
matrix_0 = [[1, 2, 3], [4, 5, 6]]
matrix_0_t = [[1, 4], [2, 5], [3, 6]]
matrix_1 = [[11, 22, 33], [44, 55, 66]]
matrix_1_t = [[11, 44], [22, 55], [33, 66]]
batch_matrix = [matrix_0, matrix_1]  # Shape (2, 2, 3)
expected_transposed = [matrix_0_t, matrix_1_t]  # Shape (2, 3, 2)
transposed = array_ops.matrix_transpose(batch_matrix)
self.assertEqual((2, 3, 2), transposed.get_shape())
self.assertAllEqual(expected_transposed, transposed)
