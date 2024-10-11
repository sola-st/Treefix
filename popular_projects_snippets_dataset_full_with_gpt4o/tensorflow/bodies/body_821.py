# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_diag_ops_test.py
for align in alignment_list:
    for _, tests in [square_cases(align)]:
        for diag_index, (vecs, solution) in tests.items():
            params = {"diagonal": vecs, "k": diag_index, "align": align}
            self._assertOpOutputMatchesExpected(params, solution)
