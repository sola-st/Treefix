# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_combine_first.py
ser1 = Series(
    pd.DatetimeIndex(["20150101", "20150102", "20150103"], tz=tz_naive_fixture),
    name="ser1",
)
ser2 = Series(
    pd.DatetimeIndex(["20160514", "20160515", "20160516"], tz=tz_naive_fixture),
    index=[2, 3, 4],
    name="ser2",
)
result = ser1.combine_first(ser2)
exp_vals = pd.DatetimeIndex(
    ["20150101", "20150102", "20150103", "20160515", "20160516"],
    tz=tz_naive_fixture,
)
exp = Series(exp_vals, name="ser1")
tm.assert_series_equal(exp, result)
