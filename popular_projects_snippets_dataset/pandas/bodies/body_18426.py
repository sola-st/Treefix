# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#19276
# tzaware DatetimeIndex should not raise when compared to NaT
op = comparison_op

dti = DatetimeIndex(
    ["2014-01-01", NaT, "2014-03-01", NaT, "2014-05-01", "2014-07-01"]
)
expected = np.array([op == operator.ne] * len(dti))
result = op(dti, NaT)
tm.assert_numpy_array_equal(result, expected)

result = op(dti.tz_localize("US/Pacific"), NaT)
tm.assert_numpy_array_equal(result, expected)
