# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#46406
df = DataFrame([[1.0, 0.0, 1.5], [0.0, 2.0, 0.0]], dtype=SparseDtype(float))
result = getattr(df, indexer)[0]
expected = Series([1.0, 0.0, 1.5], dtype=SparseDtype(float), name=0)
tm.assert_series_equal(result, expected)
