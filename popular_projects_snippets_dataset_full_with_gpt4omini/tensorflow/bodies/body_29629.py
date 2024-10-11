# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
with self.cached_session():
    # Stores expected num_rows and num_cols (when the other is given).
    # expected[d_lower, d_upper] = (expected_num_rows, expected_num_cols)
    test_list = list()

    # Square cases:
    expected = {
        (-1, -1): (5, 4),
        (-4, -3): (5, 2),
        (-2, 1): (5, 5),
        (2, 4): (3, 5),
    }
    # Do not change alignment yet. Re-alignment needs to happen after the
    # solution shape is updated.
    test_list.append((expected, square_cases()))

    # More cases:
    expected = {(-3, -1): (5, 4), (-1, 1): (4, 4), (2, 4): (4, 6)}
    test_list.append((expected, self._moreCases()))

    # Tall cases
    expected = {
        (0, 0): (3, 3),
        (-4, -3): (5, 2),
        (-2, -1): (4, 3),
        (-2, 1): (3, 3),
        (1, 2): (2, 3)
    }
    test_list.append((expected, tall_cases()))

    # Fat cases
    expected = {
        (2, 2): (2, 4),
        (-2, 0): (3, 3),
        (-1, 1): (3, 3),
        (0, 3): (3, 3)
    }
    test_list.append((expected, fat_cases()))

    for padding_value, align in zip_to_first_list_length([0, 555, -11],
                                                         alignment_list):
        # Giving both num_rows and num_cols
        for _, tests in [tall_cases(align), fat_cases(align)]:
            for diags, (vecs, solution) in tests.items():
                v_diags = array_ops.matrix_diag(
                    vecs,
                    k=diags,
                    num_rows=solution.shape[-2],
                    num_cols=solution.shape[-1],
                    padding_value=padding_value,
                    align=align)
                mask = solution == 0
                solution = solution + padding_value * mask
                self.assertEqual(v_diags.get_shape(), solution.shape)
                self.assertAllEqual(v_diags, solution)

        # Giving just num_rows.
        for expected, (_, tests) in test_list:
            for diags, (_, new_num_cols) in expected.items():
                vecs, solution = tests[diags]
                solution = solution.take(indices=range(new_num_cols), axis=-1)
                # Repacks the diagonal input according to the new solution shape.
                vecs = repack_diagonals(
                    vecs, diags, solution.shape[-2], new_num_cols, align=align)
                v_diags = array_ops.matrix_diag(
                    vecs,
                    k=diags,
                    num_rows=solution.shape[-2],
                    padding_value=padding_value,
                    align=align)
                mask = solution == 0
                solution = solution + padding_value * mask
                self.assertEqual(v_diags.get_shape(), solution.shape)
                self.assertAllEqual(v_diags, solution)

        # Giving just num_cols.
        for expected, (_, tests) in test_list:
            for diags, (new_num_rows, _) in expected.items():
                vecs, solution = tests[diags]
                solution = solution.take(indices=range(new_num_rows), axis=-2)
                # Repacks the diagonal input according to the new solution shape.
                vecs = repack_diagonals(
                    vecs, diags, new_num_rows, solution.shape[-1], align=align)
                v_diags = array_ops.matrix_diag(
                    vecs,
                    k=diags,
                    num_cols=solution.shape[-1],
                    padding_value=padding_value,
                    align=align)
                mask = solution == 0
                solution = solution + padding_value * mask
                self.assertEqual(v_diags.get_shape(), solution.shape)
                self.assertAllEqual(v_diags, solution)
