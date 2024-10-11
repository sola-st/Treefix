# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
# see gh-19891
ser = Series(date_range("20180101", periods=3, tz=tz))
result, result_bins = cut(ser, 2, retbins=True)

expected = cut(ser, result_bins)
tm.assert_series_equal(result, expected)

expected_bins = DatetimeIndex(
    ["2017-12-31 23:57:07.200000", "2018-01-02 00:00:00", "2018-01-03 00:00:00"]
)
expected_bins = expected_bins.tz_localize(tz)
tm.assert_index_equal(result_bins, expected_bins)
