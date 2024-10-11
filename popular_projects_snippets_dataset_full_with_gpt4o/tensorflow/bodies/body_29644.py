# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
with self.session():
    mat = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    mat_diag = array_ops.matrix_diag_part(mat)
    self.assertAllEqual(mat_diag, np.array([1.0, 5.0]))
    mat = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    mat_diag = array_ops.matrix_diag_part(mat)
    self.assertAllEqual(mat_diag, np.array([1.0, 4.0]))

    # Diagonal bands.
    for align in alignment_list:
        for mat, tests in [tall_cases(align), fat_cases(align)]:
            for diags, pair in tests.items():
                solution, _ = pair
                mat_diag = array_ops.matrix_diag_part(
                    mat[0], k=diags, align=align)
                self.assertEqual(mat_diag.get_shape(), solution[0].shape)
                self.assertAllEqual(mat_diag, solution[0])
