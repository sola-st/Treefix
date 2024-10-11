# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_diag_ops_test.py
for align in alignment_list:
    for _, tests in all_tests(align):
        for diag_index, (vecs, banded_mat) in tests.items():
            mask = (banded_mat == 0)
            input_mat = np.random.randint(10, size=mask.shape)
            solution = input_mat * mask + banded_mat
            self._assertOpOutputMatchesExpected(
                {
                    "input": input_mat,
                    "diagonal": vecs,
                    "k": diag_index,
                    "align": align
                }, solution)
