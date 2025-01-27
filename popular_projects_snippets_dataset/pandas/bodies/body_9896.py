# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_quantile.py
compare_func = partial(scoreatpercentile, per=q)
result = series.rolling(50, step=step).quantile(q)
assert isinstance(result, Series)
end = range(0, len(series), step or 1)[-1] + 1
tm.assert_almost_equal(result.iloc[-1], compare_func(series[end - 50 : end]))
