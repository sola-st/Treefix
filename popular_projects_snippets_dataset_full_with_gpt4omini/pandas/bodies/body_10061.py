# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_functions.py
result = getattr(frame.rolling(50, step=step), roll_func)(**kwargs)
assert isinstance(result, DataFrame)
end = range(0, len(frame), step or 1)[-1] + 1
tm.assert_series_equal(
    result.iloc[-1, :],
    frame.iloc[end - 50 : end, :].apply(compare_func, axis=0, raw=raw),
    check_names=False,
)
