# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#18849
# GH#10699 array of offsets

tz = tz_naive_fixture
dti = date_range("2017-01-01", periods=2, tz=tz)
dtarr = tm.box_expected(dti, box_with_array)

other = np.array([pd.offsets.MonthEnd(), pd.offsets.Day(n=2)])
expected = DatetimeIndex([op(dti[n], other[n]) for n in range(len(dti))])
expected = tm.box_expected(expected, box_with_array).astype(object)

if box_other:
    other = tm.box_expected(other, box_with_array)
    if box_with_array is pd.array and op is roperator.radd:
        # We expect a PandasArray, not ndarray[object] here
        expected = pd.array(expected, dtype=object)

with tm.assert_produces_warning(PerformanceWarning):
    res = op(dtarr, other)

tm.assert_equal(res, expected)
