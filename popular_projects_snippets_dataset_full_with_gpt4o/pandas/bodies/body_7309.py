# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_setops.py
# GH 24966 test for 0-len intersections are copied
index_1 = timedelta_range("1 day", periods=0, freq="h")
index_2 = timedelta_range("1 day", periods=3, freq="h")
result = index_1.intersection(index_2, sort=sort)
assert index_1 is not result
assert index_2 is not result
tm.assert_copy(result, index_1)
