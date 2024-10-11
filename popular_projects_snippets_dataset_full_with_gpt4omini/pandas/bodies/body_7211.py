# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_astype.py
# GH#12881
# a float astype int
idx = Index([0, 1, 2], dtype=np.float64)
result = idx.astype(dtype)
assert isinstance(result, Index) and result.dtype == dtype
