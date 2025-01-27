# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_test.py
for (t_a, t_b, adj_a, adj_b) in itertools.product(*(([False, True],) * 4)):
    if (t_a and adj_a) or (t_b and adj_b):
        continue
    self._testSparseSparse(t_a, t_b, adj_a, adj_b)
