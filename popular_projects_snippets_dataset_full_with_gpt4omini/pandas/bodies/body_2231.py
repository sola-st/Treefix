# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# gh-11276, gh-11745
# for origin as julian

result = Series(to_datetime(julian_dates, unit="D", origin="julian"))
expected = Series(
    to_datetime(julian_dates - Timestamp(0).to_julian_date(), unit="D")
)
tm.assert_series_equal(result, expected)
