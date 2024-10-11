# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_setops.py
# GH14323: Difference of TimedeltaIndex should not preserve frequency

index = timedelta_range("0 days", "5 days", freq="D")

other = timedelta_range("1 days", "4 days", freq="D")
expected = TimedeltaIndex(["0 days", "5 days"], freq=None)
idx_diff = index.difference(other, sort)
tm.assert_index_equal(idx_diff, expected)
tm.assert_attr_equal("freq", idx_diff, expected)

other = timedelta_range("2 days", "5 days", freq="D")
idx_diff = index.difference(other, sort)
expected = TimedeltaIndex(["0 days", "1 days"], freq=None)
tm.assert_index_equal(idx_diff, expected)
tm.assert_attr_equal("freq", idx_diff, expected)
