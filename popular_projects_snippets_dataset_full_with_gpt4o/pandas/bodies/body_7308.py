# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_setops.py
# GH 24471 test for non overlap the intersection should be zero length
index_1 = timedelta_range("1 day", periods=period_1, freq="h")
index_2 = timedelta_range("1 day", periods=period_2, freq="h")
expected = timedelta_range("1 day", periods=0, freq="h")
result = index_1.intersection(index_2, sort=sort)
tm.assert_index_equal(result, expected)
