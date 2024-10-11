# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_diag_ops_test.py
for padding_value, align in zip_to_first_list_length([555, -11],
                                                     alignment_list):
    for _, tests in all_tests(align):
        for diag_index, (vecs, solution) in tests.items():
            mask = (solution == 0)
            solution = solution + (mask * padding_value)
            self._assertOpOutputMatchesExpected(
                {
                    "diagonal": vecs,
                    "k": diag_index,
                    "num_rows": solution.shape[-2],
                    "num_cols": solution.shape[-1],
                    "padding_value": padding_value,
                    "align": align
                }, solution)
