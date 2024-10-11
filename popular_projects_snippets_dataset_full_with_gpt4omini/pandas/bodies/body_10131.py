# Extracted from ./data/repos/pandas/pandas/tests/window/test_apply.py
result = series.rolling(50).apply(f, raw=raw)
assert isinstance(result, Series)
tm.assert_almost_equal(result.iloc[-1], np.mean(series[-50:]))
