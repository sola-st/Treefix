# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# https://github.com/pandas-dev/pandas/issues/10329

tz = tz_naive_fixture

obj1 = date_range("2012-01-01", periods=3, tz=tz)
obj2 = [time(i, i, i) for i in range(3)]

obj1 = tm.box_expected(obj1, box_with_array)
obj2 = tm.box_expected(obj2, box_with_array)

msg = "|".join(
    [
        "unsupported operand",
        "cannot subtract DatetimeArray from ndarray",
    ]
)

with warnings.catch_warnings(record=True):
    # pandas.errors.PerformanceWarning: Non-vectorized DateOffset being
    # applied to Series or DatetimeIndex
    # we aren't testing that here, so ignore.
    warnings.simplefilter("ignore", PerformanceWarning)

    assert_invalid_addsub_type(obj1, obj2, msg=msg)
