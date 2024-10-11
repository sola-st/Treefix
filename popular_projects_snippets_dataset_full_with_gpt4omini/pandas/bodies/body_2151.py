# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py

# GH13834
epoch = 1370745748
ser = Series([epoch + t for t in np.arange(0, 2, 0.25)] + [iNaT]).astype(float)
result = to_datetime(ser, unit="s")
expected = Series(
    [
        Timestamp("2013-06-09 02:42:28") + timedelta(seconds=t)
        for t in np.arange(0, 2, 0.25)
    ]
    + [NaT]
)
# GH20455 argument will incur floating point errors but no premature rounding
result = result.round("ms")
tm.assert_series_equal(result, expected)
