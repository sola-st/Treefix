# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
with self.cached_session():
    v_batch = np.array([[-1.0, 0.0, -3.0], [-4.0, -5.0, -6.0]]).astype(dtype)
    mat_batch = np.array([[[1.0, 0.0, 3.0], [0.0, 2.0, 0.0], [1.0, 0.0, 3.0]],
                          [[4.0, 0.0, 4.0], [0.0, 5.0, 0.0],
                           [2.0, 0.0, 6.0]]]).astype(dtype)

    mat_set_diag_batch = np.array([[[-1.0, 0.0, 3.0], [0.0, 0.0, 0.0],
                                    [1.0, 0.0, -3.0]],
                                   [[-4.0, 0.0, 4.0], [0.0, -5.0, 0.0],
                                    [2.0, 0.0, -6.0]]]).astype(dtype)

    output = array_ops.matrix_set_diag(mat_batch, v_batch)
    self.assertEqual((2, 3, 3), output.get_shape())
    self.assertAllEqual(mat_set_diag_batch, self.evaluate(output))

    # Diagonal bands.
    for align in alignment_list:
        _, tests = square_cases(align)
        for diags, (vecs, banded_mat) in tests.items():
            mask = banded_mat == 0
            input_mat = np.random.randint(10, size=mask.shape).astype(dtype)
            solution = (input_mat * mask + banded_mat).astype(dtype)
            output = array_ops.matrix_set_diag(
                input_mat, vecs.astype(dtype), k=diags, align=align)
            self.assertEqual(output.get_shape(), solution.shape)
            self.assertAllEqual(output, solution)
