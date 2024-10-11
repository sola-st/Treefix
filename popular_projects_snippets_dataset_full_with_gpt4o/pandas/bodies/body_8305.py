# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
left = DatetimeIndex(["2012-05-11 15:19:49.695000"])
right = DatetimeIndex(
    [
        "2012-05-29 13:04:21.322000",
        "2012-05-11 15:27:24.873000",
        "2012-05-11 15:31:05.350000",
    ]
)

result = left.union(right, sort=sort)
exp = DatetimeIndex(
    [
        "2012-05-11 15:19:49.695000",
        "2012-05-29 13:04:21.322000",
        "2012-05-11 15:27:24.873000",
        "2012-05-11 15:31:05.350000",
    ]
)
if sort is None:
    exp = exp.sort_values()
tm.assert_index_equal(result, exp)
