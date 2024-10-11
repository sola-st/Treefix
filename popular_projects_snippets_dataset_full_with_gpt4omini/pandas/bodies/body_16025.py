# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_describe.py
ser = Series([0, 1, 2, 3, 4], name="int_data")
result = ser.describe()
expected = Series(
    [5, 2, ser.std(), 0, 1, 2, 3, 4],
    name="int_data",
    index=["count", "mean", "std", "min", "25%", "50%", "75%", "max"],
)
tm.assert_series_equal(result, expected)
