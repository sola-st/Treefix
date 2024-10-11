# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_astype.py
index = Index([1.0, np.nan, 0.2], dtype="object")
result = index.astype(float)
expected = Index([1.0, np.nan, 0.2], dtype=np.float64)
assert result.dtype == expected.dtype
tm.assert_index_equal(result, expected)
