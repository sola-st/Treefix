# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append_common.py
tz = tz_aware_fixture
# GH 13660

# different tz coerces to object
dti1 = pd.DatetimeIndex(["2011-01-01", "2011-01-02"], tz=tz)
dti2 = pd.DatetimeIndex(["2012-01-01", "2012-01-02"])

exp = Index(
    [
        pd.Timestamp("2011-01-01", tz=tz),
        pd.Timestamp("2011-01-02", tz=tz),
        pd.Timestamp("2012-01-01"),
        pd.Timestamp("2012-01-02"),
    ],
    dtype=object,
)

res = dti1.append(dti2)
tm.assert_index_equal(res, exp)

dts1 = Series(dti1)
dts2 = Series(dti2)
res = dts1._append(dts2)
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))

res = pd.concat([dts1, dts2])
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))

# different tz
dti3 = pd.DatetimeIndex(["2012-01-01", "2012-01-02"], tz="US/Pacific")

exp = Index(
    [
        pd.Timestamp("2011-01-01", tz=tz),
        pd.Timestamp("2011-01-02", tz=tz),
        pd.Timestamp("2012-01-01", tz="US/Pacific"),
        pd.Timestamp("2012-01-02", tz="US/Pacific"),
    ],
    dtype=object,
)

res = dti1.append(dti3)
tm.assert_index_equal(res, exp)

dts1 = Series(dti1)
dts3 = Series(dti3)
res = dts1._append(dts3)
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))

res = pd.concat([dts1, dts3])
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
