# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_quantile.py
compare_func = partial(scoreatpercentile, per=q)
result = frame.rolling(50, step=step).quantile(q)
assert isinstance(result, DataFrame)
end = range(0, len(frame), step or 1)[-1] + 1
tm.assert_series_equal(
    result.iloc[-1, :],
    frame.iloc[end - 50 : end, :].apply(compare_func, axis=0, raw=raw),
    check_names=False,
)
