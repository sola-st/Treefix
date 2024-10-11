# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_constructors.py
import scipy.sparse

mat = scipy.sparse.eye(5, 4, format="csc")

with pytest.raises(ValueError, match="not '4'"):
    SparseArray.from_spmatrix(mat)
