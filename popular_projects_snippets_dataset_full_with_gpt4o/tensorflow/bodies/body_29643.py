# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
with self.session():
    v = np.array([1.0, 2.0, 3.0])
    mat = np.diag(v)
    mat_diag = array_ops.matrix_diag_part(mat)
    self.assertEqual((3,), mat_diag.get_shape())
    self.assertAllEqual(mat_diag, v)

    for offset in [-2, 3]:
        mat = np.diag(v, offset)
        mat_diag = array_ops.matrix_diag_part(mat, k=offset)
        self.assertEqual((3,), mat_diag.get_shape())
        self.assertAllEqual(mat_diag, v)

    # Diagonal bands.
    for align in alignment_list:
        mat, tests = square_cases(align)
        for diags, pair in tests.items():
            solution, _ = pair
            mat_diag = array_ops.matrix_diag_part(mat[0], k=diags, align=align)
            self.assertEqual(mat_diag.get_shape(), solution[0].shape)
            self.assertAllEqual(mat_diag, solution[0])
