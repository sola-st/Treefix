# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
with self.cached_session():
    v_batch = np.array([[1.0, 0.0, 3.0], [4.0, 5.0, 6.0]]).astype(dtype)
    mat_batch = np.array([[[1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 3.0]],
                          [[4.0, 0.0, 0.0], [0.0, 5.0, 0.0],
                           [0.0, 0.0, 6.0]]]).astype(dtype)
    v_batch_diag = array_ops.matrix_diag(v_batch)
    self.assertEqual((2, 3, 3), v_batch_diag.get_shape())
    self.assertAllEqual(v_batch_diag, mat_batch)

    # {Sub,Super}diagonals.
    for offset in [1, -2, 5]:
        v_batch_diag = array_ops.matrix_diag(v_batch, k=offset)
        mats = [
            np.diag(v_batch[i], offset) for i in range(0, v_batch.shape[0])
        ]
        mat_batch = np.stack(mats, axis=0)
        self.assertEqual(mat_batch.shape, v_batch_diag.get_shape())
        self.assertAllEqual(v_batch_diag, mat_batch)

    # Diagonal bands with padding_value.
    for padding_value, align in zip_to_first_list_length([0, 555, -11],
                                                         alignment_list):
        for _, tests in [self._moreCases(align), square_cases(align)]:
            for diags, (vecs, solution) in tests.items():
                v_diags = array_ops.matrix_diag(
                    vecs.astype(dtype),
                    k=diags,
                    padding_value=padding_value,
                    align=align)
                mask = solution == 0
                solution = (solution + padding_value * mask).astype(dtype)
                self.assertEqual(v_diags.get_shape(), solution.shape)
                self.assertAllEqual(v_diags, solution)
