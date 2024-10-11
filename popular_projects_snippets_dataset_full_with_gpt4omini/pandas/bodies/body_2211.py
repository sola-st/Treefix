# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
ser = Series(
    np.array(
        [
            np.nan,
            np.nan,
            "01/01/2011 00:00:00",
            "01/02/2011 00:00:00",
            "01/03/2011 00:00:00",
        ],
        dtype=object,
    )
)

result = to_datetime(ser, cache=cache)
expected = Series(
    [NaT, NaT, "2011-01-01", "2011-01-02", "2011-01-03"], dtype="datetime64[ns]"
)
tm.assert_series_equal(result, expected)
