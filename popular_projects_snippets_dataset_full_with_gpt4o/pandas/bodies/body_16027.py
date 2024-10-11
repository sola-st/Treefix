# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_describe.py

ser = Series(["a", "a", "b", "c", "d"], name="str_data")
result = ser.describe()
expected = Series(
    [5, 4, "a", 2], name="str_data", index=["count", "unique", "top", "freq"]
)
tm.assert_series_equal(result, expected)
