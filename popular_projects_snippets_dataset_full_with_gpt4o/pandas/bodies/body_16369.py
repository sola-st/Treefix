# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# https://github.com/pandas-dev/pandas/issues/36044
result = Series({"a": 1, "b": 2}.keys())
expected = Series(["a", "b"])
tm.assert_series_equal(result, expected)

result = Series({"a": 1, "b": 2}.values())
expected = Series([1, 2])
tm.assert_series_equal(result, expected)
