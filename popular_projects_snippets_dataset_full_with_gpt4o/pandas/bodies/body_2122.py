# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH35888
result = to_datetime(input, cache=cache)
tm.assert_series_equal(result, expected)
