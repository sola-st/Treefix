# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
m = [[1 + 1j, 2 + 2j, 3 + 3j], [4 + 4j, 5 + 5j, 6 + 6j]]
expected_transposed = [[1 - 1j, 4 - 4j], [2 - 2j, 5 - 5j], [3 - 3j, 6 - 6j]]
matrix = ops.convert_to_tensor(m)
transposed = array_ops.matrix_transpose(matrix, conjugate=True)
self.assertEqual((3, 2), transposed.get_shape())
self.assertAllEqual(expected_transposed, transposed)
