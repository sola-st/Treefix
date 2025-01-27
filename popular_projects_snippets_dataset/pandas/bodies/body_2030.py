# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
# with units
result = TimedeltaIndex(
    [np.timedelta64(0, "ns"), np.timedelta64(10, "s").astype("m8[ns]")]
)
expected = to_timedelta([0, 10], unit="s")
tm.assert_index_equal(result, expected)
