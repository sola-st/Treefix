# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
with self.cached_session():
    v_batch = np.array([[1.0, 0.0, 3.0], [4.0, 5.0, 6.0]]).astype(dtype)
    mat_batch = np.array([[[1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 3.0]],
                          [[4.0, 0.0, 0.0], [0.0, 5.0, 0.0],
                           [0.0, 0.0, 6.0]]]).astype(dtype)
    self.assertEqual(mat_batch.shape, (2, 3, 3))
    mat_batch_diag = array_ops.matrix_diag_part(mat_batch)
    self.assertEqual((2, 3), mat_batch_diag.get_shape())
    self.assertAllEqual(mat_batch_diag, v_batch)

    # Diagonal bands with padding_value.
    for padding_value, align in zip_to_first_list_length([0, 555, -11],
                                                         alignment_list):
        mat, tests = square_cases(align)
        for diags, pair in tests.items():
            solution, _ = pair
            mat_batch_diag = array_ops.matrix_diag_part(
                mat.astype(dtype),
                k=diags,
                padding_value=padding_value,
                align=align)
            mask = solution == 0
            solution = (solution + padding_value * mask).astype(dtype)
            self.assertEqual(mat_batch_diag.get_shape(), solution.shape)
            self.assertAllEqual(mat_batch_diag, solution)
