# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_functions.py
result = getattr(series.rolling(50, step=step), roll_func)(**kwargs)
assert isinstance(result, Series)
end = range(0, len(series), step or 1)[-1] + 1
tm.assert_almost_equal(result.iloc[-1], compare_func(series[end - 50 : end]))
