# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_describe.py
ser = Series(
    [Period("2020-01", "M"), Period("2020-01", "M"), Period("2019-12", "M")],
    name="period_data",
)
result = ser.describe()
expected = Series(
    [3, 2, ser[0], 2],
    name="period_data",
    index=["count", "unique", "top", "freq"],
)
tm.assert_series_equal(result, expected)
