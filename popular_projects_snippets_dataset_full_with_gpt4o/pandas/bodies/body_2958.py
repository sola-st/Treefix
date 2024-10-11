# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_interpolate.py
# GH 9687
periods = 5
idx = date_range(start="2014-01-01", periods=periods)
data = np.random.rand(periods, periods)
data[data < 0.5] = np.nan
expected = DataFrame(index=idx, columns=idx, data=data)

result = expected.interpolate(axis=0, method="time")
return_value = expected.interpolate(axis=0, method="time", inplace=True)
assert return_value is None
tm.assert_frame_equal(result, expected)
