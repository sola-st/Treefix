# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_to_series.py
naive = DatetimeIndex(["2013-1-1 13:00", "2013-1-2 14:00"], name="B")
idx = naive.tz_localize("US/Pacific")

expected = Series(np.array(idx.tolist(), dtype="object"), name="B")
result = idx.to_series(index=[0, 1])
assert expected.dtype == idx.dtype
tm.assert_series_equal(result, expected)
