# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
for dtype in (dtypes.float32, dtypes.float64):
    for conjugate in (True, False):
        with self.subTest(complex_type=dtype, conjugate=conjugate):
            vector = math_ops.complex(
                constant_op.constant(0, dtype=dtype),
                math_ops.range(96, dtype=dtype))
            column_vector = array_ops.expand_dims(vector, axis=-1)
            row_vector = array_ops.expand_dims(vector, axis=0)
            narrow_matrix = array_ops.tile(column_vector, [1, 2])  # [96, 2]
            expected_transposed = array_ops.tile(row_vector, [2, 1])  # [2, 96]
            if conjugate:
                expected_transposed = -expected_transposed

            transposed = array_ops.matrix_transpose(
                narrow_matrix, conjugate=conjugate)

            self.assertEqual((2, 96), transposed.get_shape())
            self.assertAllEqual(expected_transposed, transposed)
