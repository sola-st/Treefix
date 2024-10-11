# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#18849, GH#19744
other_box = index_or_series

tz = tz_naive_fixture
dti = date_range("2017-01-01", periods=2, tz=tz, name=names[0])
other = other_box([pd.offsets.MonthEnd(), pd.offsets.Day(n=2)], name=names[1])

xbox = get_upcast_box(dti, other)

with tm.assert_produces_warning(PerformanceWarning):
    res = op(dti, other)

expected = DatetimeIndex(
    [op(dti[n], other[n]) for n in range(len(dti))], name=names[2], freq="infer"
)
expected = tm.box_expected(expected, xbox).astype(object)
tm.assert_equal(res, expected)
