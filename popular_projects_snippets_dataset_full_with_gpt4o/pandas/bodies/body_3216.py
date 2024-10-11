# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asfreq.py
# https://github.com/pandas-dev/pandas/issues/50727
result = DatetimeIndex(
    date_range("2000", periods=2).as_unit(unit).normalize(), freq="D"
)
expected = DatetimeIndex(["2000-01-01", "2000-01-02"], freq="D").as_unit(unit)
tm.assert_index_equal(result, expected)
