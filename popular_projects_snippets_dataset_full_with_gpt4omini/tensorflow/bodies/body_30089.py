# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
matrix = [[1, 2, 3]]
matrix_squeezed = array_ops.squeeze(matrix, [0])
self.assertEqual(matrix_squeezed.get_shape(), (3))

with self.assertRaisesRegex(
    Exception, "Can not squeeze dim.1., expected a dimension of 1, got 3"):
    matrix_squeezed = array_ops.squeeze(matrix, [1])
