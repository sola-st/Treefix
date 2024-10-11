# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
with self.session():
    v_batch = np.array([[1.0, 2.0], [4.0, 5.0]])
    mat_batch = np.array([[[1.0, 0.0, 0.0], [0.0, 2.0, 0.0]],
                          [[4.0, 0.0, 0.0], [0.0, 5.0, 0.0]]])
    self.assertEqual(mat_batch.shape, (2, 2, 3))
    mat_batch_diag = array_ops.matrix_diag_part(mat_batch)
    self.assertEqual((2, 2), mat_batch_diag.get_shape())
    self.assertAllEqual(mat_batch_diag, v_batch)

    # Diagonal bands with padding_value and align.
    for padding_value, align in zip_to_first_list_length([0, 555, -11],
                                                         alignment_list):
        for mat, tests in [tall_cases(align), fat_cases(align)]:
            for diags, pair in tests.items():
                solution, _ = pair
                mat_batch_diag = array_ops.matrix_diag_part(
                    mat, k=diags, padding_value=padding_value, align=align)
                mask = solution == 0
                solution = solution + padding_value * mask
                self.assertEqual(mat_batch_diag.get_shape(), solution.shape)
                self.assertAllEqual(mat_batch_diag, solution)
