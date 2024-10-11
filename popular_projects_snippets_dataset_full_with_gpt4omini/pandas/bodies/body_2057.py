# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# Explicit cast to float to explicit cast when setting np.nan
ser = Series([19801222, 19801222] + [19810105] * 5, dtype="float")
# with NaT
expected = Series(
    [Timestamp("19801222"), Timestamp("19801222")] + [Timestamp("19810105")] * 5
)
expected[2] = np.nan
ser[2] = np.nan

result = to_datetime(ser, format="%Y%m%d", cache=cache)
tm.assert_series_equal(result, expected)

# string with NaT
ser2 = ser.apply(str)
ser2[2] = "nat"
with pytest.raises(
    ValueError, match='unconverted data remains: ".0", at position 0'
):
    # https://github.com/pandas-dev/pandas/issues/50051
    to_datetime(ser2, format="%Y%m%d", cache=cache)
