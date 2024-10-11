# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_astype.py
# mixed int-float
idx = Index([1.5, 2, 3, 4, 5], dtype=np.float64)
idx.name = "foo"
result = idx.astype(object)
assert result.equals(idx)
assert idx.equals(result)
assert isinstance(result, Index) and result.dtype == object
