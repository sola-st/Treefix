# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
data = frame_or_series(np.array(list(range(10)) + [np.nan] * 10))
result = getattr(data.expanding(min_periods=1, axis=0), func)()
assert isinstance(result, frame_or_series)

expected = static_comp(data[:11])
if frame_or_series is Series:
    tm.assert_almost_equal(result[10], expected)
else:
    tm.assert_series_equal(result.iloc[10], expected, check_names=False)
