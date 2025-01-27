# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
engine, raw = engine_and_raw
data = frame_or_series(np.array(list(range(10)) + [np.nan] * 10))
result = data.expanding(min_periods=1).apply(
    lambda x: x.mean(), raw=raw, engine=engine
)
assert isinstance(result, frame_or_series)

if frame_or_series is Series:
    tm.assert_almost_equal(result[9], np.mean(data[:11], axis=0))
else:
    tm.assert_series_equal(
        result.iloc[9], np.mean(data[:11], axis=0), check_names=False
    )
