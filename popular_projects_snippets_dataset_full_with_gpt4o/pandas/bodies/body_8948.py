# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_accessor.py
# gh-26554
import scipy.sparse

m = scipy.sparse.csr_matrix(np.array([[0, 1], [0, 0]]))
with pytest.raises(
    TypeError, match="Expected coo_matrix. Got csr_matrix instead."
):
    pd.Series.sparse.from_coo(m)
