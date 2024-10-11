# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_drop_duplicates.py
# to check Index/Series compat
idx = idx.append(idx[:5])

tm.assert_numpy_array_equal(idx.duplicated(keep=keep), expected)
expected = idx[~expected]

result = idx.drop_duplicates(keep=keep)
tm.assert_index_equal(result, expected)

result = Series(idx).drop_duplicates(keep=keep)
expected = Series(expected, index=index)
tm.assert_series_equal(result, expected)
