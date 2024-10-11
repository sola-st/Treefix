# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# don't cast a DatetimeIndex WITH a tz, leave as object
# GH#6032
naive = DatetimeIndex(["2013-1-1 13:00", "2013-1-2 14:00"], name="B")
idx = naive.tz_localize("US/Pacific")

expected = Series(np.array(idx.tolist(), dtype="object"), name="B")
assert expected.dtype == idx.dtype

# convert index to series
result = Series(idx)
tm.assert_series_equal(result, expected)
