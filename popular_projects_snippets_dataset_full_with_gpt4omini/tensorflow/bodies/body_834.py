# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_diag_ops_test.py
for align in alignment_list:
    test_list = [square_cases(align), tall_cases(align), fat_cases(align)]
    for mat, tests in test_list:
        for diag_index, (solution, _) in tests.items():
            self._assertOpOutputMatchesExpected(
                {
                    "input": mat[0],
                    "k": diag_index,
                    "align": align
                }, solution[0])
