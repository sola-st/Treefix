# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rename_axis.py
# GH 15704
expected = datetime_series.rename_axis("foo")
result = datetime_series
no_return = result.rename_axis("foo", inplace=True)

assert no_return is None
tm.assert_series_equal(result, expected)
