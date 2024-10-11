# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
values = index_or_series(["1/1/2000", "1/2/2000", "1/3/2000"])
result = to_datetime(values, format=format, cache=cache)
expected = index_or_series(expected)
if isinstance(expected, Series):
    tm.assert_series_equal(result, expected)
else:
    tm.assert_index_equal(result, expected)
