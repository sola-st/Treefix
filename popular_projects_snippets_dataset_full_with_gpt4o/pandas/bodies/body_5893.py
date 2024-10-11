# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
# pre-2.0 this would give a SparseDtype even if the user asked
#  for a non-sparse dtype.
result = pd.Series(data[:5]).astype(str)
expected = pd.Series([str(x) for x in data[:5]], dtype=object)
self.assert_series_equal(result, expected)
