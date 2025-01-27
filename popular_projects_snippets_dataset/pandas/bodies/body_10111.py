# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
result = getattr(frame.ewm(span=10, min_periods=5), func)()
result = result.loc[(slice(None), 1), 5]
result.index = result.index.droplevel(1)
expected = getattr(frame[1].ewm(span=10, min_periods=5), func)(frame[5])
tm.assert_series_equal(result, expected, check_names=False)
