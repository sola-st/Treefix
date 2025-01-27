# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH#7207, GH#11128
# test .dt namespace accessor

# timedelta index
cases = [
    Series(
        timedelta_range("1 day", periods=5), index=list("abcde"), name="xxx"
    ),
    Series(timedelta_range("1 day 01:23:45", periods=5, freq="s"), name="xxx"),
    Series(
        timedelta_range("2 days 01:23:45.012345", periods=5, freq="ms"),
        name="xxx",
    ),
]
for ser in cases:
    for prop in ok_for_td:
        # we test freq below
        if prop != "freq":
            self._compare(ser, prop)

    for prop in ok_for_td_methods:
        getattr(ser.dt, prop)

    result = ser.dt.components
    assert isinstance(result, DataFrame)
    tm.assert_index_equal(result.index, ser.index)

    result = ser.dt.to_pytimedelta()
    assert isinstance(result, np.ndarray)
    assert result.dtype == object

    result = ser.dt.total_seconds()
    assert isinstance(result, Series)
    assert result.dtype == "float64"

    freq_result = ser.dt.freq
    assert freq_result == TimedeltaIndex(ser.values, freq="infer").freq
