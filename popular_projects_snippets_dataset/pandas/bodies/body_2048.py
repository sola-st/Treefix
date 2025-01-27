# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
# GH 35574
expected = Series([timedelta(days=1), expected_val])
result = to_timedelta(Series([1, result_val], dtype="Int64"), unit="days")

tm.assert_series_equal(result, expected)
