# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
with self.session():
    v = np.array([1.0, 2.0, 3.0])
    mat = np.diag(v)
    v_diag = array_ops.matrix_diag(v)
    self.assertEqual((3, 3), v_diag.get_shape())
    self.assertAllEqual(v_diag, mat)

    # {Sub,Super}diagonals.
    for offset in [1, -2, 5]:
        mat = np.diag(v, offset)
        v_diag = array_ops.matrix_diag(v, k=offset)
        self.assertEqual(mat.shape, v_diag.get_shape())
        self.assertAllEqual(v_diag, mat)

    # Diagonal bands.
    for align in alignment_list:
        for _, tests in [self._moreCases(align), square_cases(align)]:
            for diags, (vecs, solution) in tests.items():
                v_diags = array_ops.matrix_diag(vecs[0], k=diags, align=align)
                self.assertEqual(v_diags.get_shape(), solution[0].shape)
                self.assertAllEqual(v_diags, solution[0])
