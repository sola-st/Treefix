# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_period.py
# GH#7606 without freq
idx = DatetimeIndex(["2011-01-01", "2011-01-02", "2011-01-03", "2011-01-04"])
exp_idx = PeriodIndex(
    ["2011-01-01", "2011-01-02", "2011-01-03", "2011-01-04"], freq="D"
)

obj = DataFrame(np.random.randn(4, 4), index=idx, columns=idx)
obj = tm.get_obj(obj, frame_or_series)
expected = obj.copy()
expected.index = exp_idx
tm.assert_equal(obj.to_period(), expected)

if frame_or_series is DataFrame:
    expected = obj.copy()
    expected.columns = exp_idx
    tm.assert_frame_equal(obj.to_period(axis=1), expected)
