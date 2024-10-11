# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_accessor.py
ser = pd.Series([0, 1, 0, 10], dtype="Sparse[int64]")
result = ser.sparse.to_dense()
expected = pd.Series([0, 1, 0, 10])
tm.assert_series_equal(result, expected)
