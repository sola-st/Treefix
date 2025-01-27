# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_insert.py
idx = DatetimeIndex(["2017-01-01"], tz=tz)

item = np.timedelta64("NaT")
result = idx.insert(0, item)
expected = Index([item] + list(idx), dtype=object)
tm.assert_index_equal(result, expected)
