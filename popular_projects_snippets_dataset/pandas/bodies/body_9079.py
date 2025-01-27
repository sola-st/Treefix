# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_combine_concat.py
# https://github.com/pandas-dev/pandas/issues/34336
s_sparse = pd.Series([1, 0, 2], dtype=pd.SparseDtype("int64", 0))

result = pd.concat([s_sparse, other], ignore_index=True)
expected = pd.Series(list(s_sparse) + list(other)).astype(expected_dtype)
tm.assert_series_equal(result, expected)

result = pd.concat([other, s_sparse], ignore_index=True)
expected = pd.Series(list(other) + list(s_sparse)).astype(expected_dtype)
tm.assert_series_equal(result, expected)
