# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_diag_ops_test.py
# Stores expected num_rows and num_cols (when the other is given).
# expected[(d_lower, d_upper)] = (expected_num_rows, expected_num_cols)
test_list = list()

# Do not align the test cases here. Re-alignment needs to happen after the
# solution shape is updated.
# Square cases:
expected = {
    (-1, -1): (5, 4),
    (-4, -3): (5, 2),
    (-2, 1): (5, 5),
    (2, 4): (3, 5),
}
test_list.append((expected, square_cases()))

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

# Giving both num_rows and num_cols
align = alignment_list[0]
for _, tests in [tall_cases(align), fat_cases(align)]:
    for diag_index, (vecs, solution) in tests.items():
        self._assertOpOutputMatchesExpected(
            {
                "diagonal": vecs,
                "k": diag_index,
                "num_rows": solution.shape[-2],
                "num_cols": solution.shape[-1],
                "align": align
            }, solution)

    # We go through each alignment in a round-robin manner.
align_index = 0

# Giving just num_rows or num_cols.
for expected, (_, tests) in test_list:
    for diag_index, (new_num_rows, new_num_cols) in expected.items():
        align = alignment_list[align_index]
        align_index = (align_index + 1) % len(alignment_list)
        vecs, solution = tests[diag_index]
        solution_given_num_rows = solution.take(
            indices=range(new_num_cols), axis=-1)
        # Repacks the diagonal input according to the new solution shape.
        vecs_given_num_rows = repack_diagonals(
            vecs,
            diag_index,
            solution_given_num_rows.shape[-2],
            new_num_cols,
            align=align)
        self._assertOpOutputMatchesExpected(
            {
                "diagonal": vecs_given_num_rows,
                "k": diag_index,
                "num_rows": solution_given_num_rows.shape[-2],
                "align": align
            }, solution_given_num_rows)
        solution_given_num_cols = solution.take(
            indices=range(new_num_rows), axis=-2)
        # Repacks the diagonal input according to the new solution shape.
        vecs_given_num_cols = repack_diagonals(
            vecs,
            diag_index,
            new_num_rows,
            solution_given_num_cols.shape[-1],
            align=align)
        self._assertOpOutputMatchesExpected(
            {
                "diagonal": vecs_given_num_cols,
                "k": diag_index,
                "num_cols": solution_given_num_cols.shape[-1],
                "align": align
            }, solution_given_num_cols)
