# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
series = Series([["a"]] * 100)
result = to_datetime(series, errors="ignore", cache=cache)
tm.assert_series_equal(series, result)
