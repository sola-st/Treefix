# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# https://github.com/pandas-dev/pandas/issues/50237
# Explicit cast to float to explicit cast when setting np.nan
ser = Series([198012, 198012] + [198101] * 5, dtype="float")
expected = Series(
    [Timestamp("19801201"), Timestamp("19801201")] + [Timestamp("19810101")] * 5
)
expected[2] = np.nan
ser[2] = np.nan
result = to_datetime(ser, format="%Y%m", cache=cache)
tm.assert_series_equal(result, expected)
