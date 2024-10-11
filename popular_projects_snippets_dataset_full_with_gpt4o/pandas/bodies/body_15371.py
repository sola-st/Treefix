# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# make sure the dt64 isn't cast by numpy to integers
# https://github.com/numpy/numpy/issues/12550

ser = Series({"X": np.nan}, dtype=object)

indexer = [True]

# "exact_match" -> size of array being set matches size of ser
value = np.array([4], dtype="M8[ns]")

ser.iloc[indexer] = value

expected = Series([value[0]], index=["X"], dtype=object)
assert all(isinstance(x, np.datetime64) for x in expected.values)

tm.assert_series_equal(ser, expected)
