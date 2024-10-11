# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_setops.py
index_1 = timedelta_range("1 day", periods=4, freq="h")
index_2 = index_1 + pd.offsets.Hour(5)

result = index_1.intersection(index_2)
assert len(result) == 0

index_1 = timedelta_range("1 day", periods=4, freq="h")
index_2 = index_1 + pd.offsets.Hour(1)

result = index_1.intersection(index_2)
expected = timedelta_range("1 day 01:00:00", periods=3, freq="h")
tm.assert_index_equal(result, expected)
assert result.freq == expected.freq
