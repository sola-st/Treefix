# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_describe.py
ser = Series([True, True, False, False, False], name="bool_data")
result = ser.describe()
expected = Series(
    [5, 2, False, 3], name="bool_data", index=["count", "unique", "top", "freq"]
)
tm.assert_series_equal(result, expected)
