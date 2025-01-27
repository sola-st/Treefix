# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_diag_ops_test.py
for padding_value, align in zip_to_first_list_length([555, -11],
                                                     alignment_list):
    for mat, tests in all_tests(align):
        for diag_index, (solution, _) in tests.items():
            mask = (solution == 0)
            solution = solution + (mask * padding_value)
            self._assertOpOutputMatchesExpected(
                {
                    "input": mat,
                    "k": diag_index,
                    "padding_value": padding_value,
                    "align": align
                }, solution)
