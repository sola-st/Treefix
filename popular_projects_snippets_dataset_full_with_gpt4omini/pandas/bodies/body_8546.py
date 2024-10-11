# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH#49292
val = np.datetime64(1, "D")
result = DatetimeIndex([val], tz="US/Pacific")

expected = DatetimeIndex([val.astype("M8[s]")], tz="US/Pacific")
tm.assert_index_equal(result, expected)
