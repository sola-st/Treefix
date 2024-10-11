# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append_common.py
tz = tz_aware_fixture
# GH 7795
dti1 = pd.DatetimeIndex(["2011-01-01", "2011-01-02"], tz=tz)
dti2 = pd.DatetimeIndex(["2012-01-01", "2012-01-02"], tz=tz)

exp = pd.DatetimeIndex(
    ["2011-01-01", "2011-01-02", "2012-01-01", "2012-01-02"], tz=tz
)

res = dti1.append(dti2)
tm.assert_index_equal(res, exp)

dts1 = Series(dti1)
dts2 = Series(dti2)
res = dts1._append(dts2)
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))

res = pd.concat([dts1, dts2])
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
