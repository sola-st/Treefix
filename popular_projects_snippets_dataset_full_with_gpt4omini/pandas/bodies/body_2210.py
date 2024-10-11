# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
ser = Series(
    np.array(
        ["01/01/2011 00:00:00", np.nan, "01/03/2011 00:00:00", np.nan],
        dtype=object,
    )
)
result = to_datetime(ser, cache=cache)
expected = Series(
    ["2011-01-01", NaT, "2011-01-03", NaT], dtype="datetime64[ns]"
)
tm.assert_series_equal(result, expected)
